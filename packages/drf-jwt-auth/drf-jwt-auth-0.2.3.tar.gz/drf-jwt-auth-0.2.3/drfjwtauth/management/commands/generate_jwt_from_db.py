from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand
from datetime import datetime
from drfjwtauth.auth import JWTAuth
from drfjwtauth.serializers import JWTUserSerializer


class Command(BaseCommand):
    help = 'Generate a valid JWT from db by the username'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('-d', '--expiration_date', required=True, type=datetime.fromisoformat)


    def handle(self, *args, **options):

        try:
            # To catch the exception when auth app is disabled
            User = get_user_model()

            user_qs = User.objects.filter(username=options['username'])

            if user_qs.exists():
                user = JWTUserSerializer(user_qs.first()).data

                user[getattr(settings, 'EXPIRATION_DATE_FIELD', 'exp')] = int(options['expiration_date'].timestamp())

                token = JWTAuth.encode_token(user).decode("utf-8")

                self.stdout.write(self.style.SUCCESS(token))

            else:
                self.stdout.write(self.style.ERROR("The given username does not exists"))
        except ImproperlyConfigured:
            self.stdout.write(
                self.style.ERROR("Authentication is disabled in this project. Try with generate_jwt command instead.")
            )
