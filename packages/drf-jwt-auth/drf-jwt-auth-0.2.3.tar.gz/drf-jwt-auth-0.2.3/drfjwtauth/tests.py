import pytest
from io import StringIO
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import call_command
from unittest import TestCase

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from drfjwtauth import settings
from drfjwtauth.auth import JWTAuth
from drfjwtauth.views import VerifyJWTView

User = get_user_model()


class Request:

    def __init__(self):
        self.META = dict()
        self.data = dict()
        self.query_params = dict()


class JWTTestsUtils(object):

    def setUp(self):
        self.payload = {
            'id': 1,
            'first_name': 'Name',
            'last_name': 'Company',
            'username': 'ncompany',
            'email': 'name@company.com',
            'is_active': True,
            'is_staff': True,
            'is_superuser': False,
            'channels': ['c1', 'c2', 'c3', 'c4'],
            'groups': ['g1', 'g2'],
            'permissions': ['p1', 'p2', 'p3'],
            settings.EXPIRATION_DATE_FIELD: int((datetime.utcnow() + timedelta(days=1)).timestamp())
        }

        settings.SIGNING_KEY = 'qwertyuiop1234567890'

    def _generate_jwt(self, expired=False):
        if expired:
            self.payload[settings.EXPIRATION_DATE_FIELD] = int((datetime.utcnow() - timedelta(days=1)).timestamp())
        return JWTAuth.encode_token(self.payload).decode('utf-8')

    def _get_request_with_token_in_headers(self, token):
        request = Request()
        request.META['HTTP_AUTHORIZATION'] = f'{settings.AUTH_HEADER} {token}'
        return request


class TestJWTAuth(JWTTestsUtils, TestCase):

    def _get_request_with_token_as_query_param(self, token):
        request = Request()
        request.query_params[settings.QUERY_PARAM_NAME] = token
        return request

    def _authenticate_request(self, request):
        backend = JWTAuth()
        return backend.authenticate(request)

    def _check_user_data_is_properly_loaded(self, user):
        self.assertEqual(user.id, self.payload.get('id'))
        self.assertEqual(user.pk, self.payload.get('id'))
        self.assertEqual(user.first_name, self.payload.get('first_name'))
        self.assertEqual(user.last_name, self.payload.get('last_name'))
        self.assertEqual(user.username, self.payload.get('username'))
        self.assertEqual(user.email, self.payload.get('email'))
        self.assertEqual(user.is_active, self.payload.get('is_active'))
        self.assertEqual(user.is_staff, self.payload.get('is_staff'))
        self.assertEqual(user.is_superuser, self.payload.get('is_superuser'))
        self.assertEqual(user.channels, self.payload.get('channels'))
        self.assertEqual(user.groups, self.payload.get('groups'))
        self.assertEqual(user.permissions, self.payload.get('permissions'))

    def test_invalid_token_in_headers_raises_exception(self):
        request = self._get_request_with_token_in_headers('abc')
        with self.assertRaises(AuthenticationFailed):
            self._authenticate_request(request)

    def test_modified_token_in_headers_raises_exception(self):
        encoded_jwt = self._generate_jwt().replace('e', 'i')
        request = self._get_request_with_token_in_headers(encoded_jwt)
        with self.assertRaises(AuthenticationFailed):
            self._authenticate_request(request)

    def test_expired_token_in_headers_raises_exception(self):
        encoded_jwt = self._generate_jwt(expired=True)
        request = self._get_request_with_token_in_headers(encoded_jwt)
        with self.assertRaises(AuthenticationFailed):
            self._authenticate_request(request)

    def test_user_authenticates_in_headers_and_gets_data_loaded_properly(self):
        encoded_jwt = self._generate_jwt()
        request = self._get_request_with_token_in_headers(encoded_jwt)
        user, unused = self._authenticate_request(request)
        self._check_user_data_is_properly_loaded(user)

    def test_invalid_token_as_query_param_raises_exception(self):
        request = self._get_request_with_token_as_query_param('abc')
        with self.assertRaises(AuthenticationFailed):
            self._authenticate_request(request)

    def test_modified_token_as_query_param_raises_exception(self):
        encoded_jwt = self._generate_jwt().replace('e', 'i')
        request = self._get_request_with_token_as_query_param(encoded_jwt)
        with self.assertRaises(AuthenticationFailed):
            self._authenticate_request(request)

    def test_expired_token_as_query_param_raises_exception(self):
        encoded_jwt = self._generate_jwt(expired=True)
        request = self._get_request_with_token_as_query_param(encoded_jwt)
        with self.assertRaises(AuthenticationFailed):
            self._authenticate_request(request)

    def test_user_authenticates_as_query_param_and_gets_data_loaded_properly(self):
        encoded_jwt = self._generate_jwt()
        request = self._get_request_with_token_as_query_param(encoded_jwt)
        user, unused = self._authenticate_request(request)
        self._check_user_data_is_properly_loaded(user)


class TestVerifyJWTView(JWTTestsUtils, TestCase):

    def _get_request_with_token_data(self, token):
        request = Request()
        request.data['token'] = token
        return request

    def _make_request(self, request):
        view = VerifyJWTView()
        return view.post(request)

    def test_invalid_token_returns_400_bad_request(self):
        request = self._get_request_with_token_data('abc')
        response = self._make_request(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modified_token_returns_400_bad_request(self):
        encoded_jwt = self._generate_jwt().replace('e', 'i')
        request = self._get_request_with_token_data(encoded_jwt)
        response = self._make_request(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_expired_token_returns_400_bad_request(self):
        encoded_jwt = self._generate_jwt(expired=True)
        request = self._get_request_with_token_data(encoded_jwt)
        response = self._make_request(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_token_returns_200_ok(self):
        encoded_jwt = self._generate_jwt()
        request = self._get_request_with_token_data(encoded_jwt)
        response = self._make_request(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_without_token_returns_400_bad_request(self):
        request = Request()
        response = self._make_request(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_token_in_headers_returns_200_ok(self):
        encoded_jwt = self._generate_jwt()
        request = self._get_request_with_token_in_headers(encoded_jwt)
        response = self._make_request(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GenerateJWTCommand(JWTTestsUtils, TestCase):

    def _convert_user_dict_to_arguments(self, user_dict):

        command_args = [user_dict['username']]

        if settings.EXPIRATION_DATE_FIELD in user_dict:
            command_args = [*command_args, *['-d', datetime.fromtimestamp(user_dict[settings.EXPIRATION_DATE_FIELD]).date().isoformat()]]
        if 'id' in user_dict:
            command_args = [*command_args, *['--id', user_dict['id']]]
        if 'first_name' in user_dict:
            command_args = [*command_args, *['--first_name', user_dict['first_name']]]
        if 'last_name' in user_dict:
            command_args = [*command_args, *['--last_name', user_dict['last_name']]]
        if 'email' in user_dict:
            command_args = [*command_args, *['--email', user_dict['email']]]
        if 'channels' in user_dict:
            command_args = [*command_args, *['--channels', *user_dict['channels']]]
        if 'groups' in user_dict:
            command_args = [*command_args, *['--groups', *user_dict['groups']]]
        if 'permissions' in user_dict:
            command_args = [*command_args, *['--permissions', *user_dict['permissions']]]
        if user_dict.get('is_active'):
            command_args.append('--is_active')
        if user_dict.get('is_staff'):
            command_args.append('--is_staff')
        if user_dict.get('is_superuser'):
            command_args.append('--is_superuser')

        return command_args

    def test_jwt_generate_command_is_ok(self):
        expiration_date = (datetime.utcnow() + timedelta(days=1))
        self.payload[settings.EXPIRATION_DATE_FIELD] = int(datetime(expiration_date.year, expiration_date.month, expiration_date.day).timestamp())
        
        command_args = self._convert_user_dict_to_arguments(self.payload)

        out = StringIO()
        call_command('generate_jwt', *command_args, stdout=out)

        token_from_payload = self._generate_jwt()
        token_from_command = out.getvalue().rstrip("\n")

        self.assertEqual(token_from_payload, token_from_command)

    def test_jwt_generate_command_is_ok_with_partial_arguments(self):
        expiration_date = (datetime.utcnow() + timedelta(days=1))

        user = {
            "username": "new_user",
            settings.EXPIRATION_DATE_FIELD: int(datetime(expiration_date.year, expiration_date.month, expiration_date.day).timestamp())
        }
        
        command_args = self._convert_user_dict_to_arguments(user)

        out = StringIO()
        call_command('generate_jwt', *command_args, stdout=out)

        token_from_command = out.getvalue().rstrip("\n")
        decoded_token = JWTAuth.decode_token(token_from_command)

        self.assertEqual(decoded_token["username"], user["username"])
        self.assertEqual(decoded_token["groups"], list())

    @pytest.mark.django_db()
    def test_jwt_generate_from_db_command_is_ok(self):
        user = User(
            username="db_user",
            email="db_user@company.com"
        )
        user.save()

        user_content_type = ContentType.objects.get_for_model(User)

        test_group, was_created = Group.objects.get_or_create(name='test_group')
        unassigned_test_group, was_created = Group.objects.get_or_create(name='unassigned_test_group')

        test_permission = Permission.objects.create(codename='test_permission',
                                               name='Demo Permission',
                                               content_type=user_content_type)

        unassigned_test_permission = Permission.objects.create(codename='unassigned_test_permission',
                                               name='Unassigned Demo Permission',
                                               content_type=user_content_type)

        user.user_permissions.add(test_permission)
        user.groups.add(test_group)

        expiration_date = (datetime.utcnow() + timedelta(days=1)).strftime("%Y-%m-%d")

        out = StringIO()
        call_command('generate_jwt_from_db', user.username, '-d', expiration_date, stdout=out)

        token_from_command = out.getvalue().rstrip("\n")

        decoded_token = JWTAuth.decode_token(token_from_command)

        self.assertEqual(user.username, decoded_token.get('username'))
        self.assertIn(test_group.name, decoded_token.get('groups'))
        self.assertNotIn(unassigned_test_group.name, decoded_token.get('groups'))
        self.assertIn(test_permission.codename, decoded_token.get('permissions'))
        self.assertNotIn(unassigned_test_permission.codename, decoded_token.get('permissions'))


    @pytest.mark.django_db()
    def test_jwt_generate_from_db_command_fails_when_username_not_exists(self):
        expiration_date = (datetime.utcnow() + timedelta(days=1)).strftime("%Y-%m-%d")

        out = StringIO()
        call_command('generate_jwt_from_db', "not_existing_user", '-d', expiration_date, stdout=out)

        error_message = out.getvalue().rstrip("\n")

        self.assertEqual(error_message, "The given username does not exists")


@pytest.fixture
def test_jwt_generate_from_db_command_fails_when_auth_is_disabled(settings):
    settings.INSTALLED_APPS = ['drfjwtauth']

    expiration_date = (datetime.utcnow() + timedelta(days=1)).strftime("%Y-%m-%d")

    out = StringIO()
    call_command('generate_jwt_from_db', "not_existing_user", '-d', expiration_date, stdout=out)

    error_message = out.getvalue().rstrip("\n")

    self.assertEqual(error_message,
                     "Authentication is disabled in this project. Try with generate_jwt command instead."
    )
