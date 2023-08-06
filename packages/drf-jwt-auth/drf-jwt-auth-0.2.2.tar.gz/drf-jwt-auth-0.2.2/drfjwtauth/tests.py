from datetime import datetime, timedelta
from unittest import TestCase

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from drfjwtauth import settings
from drfjwtauth.auth import JWTAuth
from drfjwtauth.views import VerifyJWTView


class Request:

    def __init__(self):
        self.META = dict()
        self.data = dict()
        self.query_params = dict()


class JWTTestsUtils(object):

    def setUp(self):
        self.payload = {
            'id': 1,
            'fist_name': 'Name',
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
