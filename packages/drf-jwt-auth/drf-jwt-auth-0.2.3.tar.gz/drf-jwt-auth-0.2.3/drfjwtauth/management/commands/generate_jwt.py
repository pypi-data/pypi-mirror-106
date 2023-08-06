from django.conf import settings
from django.core.management.base import BaseCommand
from datetime import datetime
from drfjwtauth.auth import JWTAuth


class Command(BaseCommand):
    help = 'Generate a valid JWT with the given params'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

        parser.add_argument('-d', '--expiration_date', required=True, type=datetime.fromisoformat)

        parser.add_argument('--id', required=False, default=0, type=int)
        
        parser.add_argument('--first_name', required=False, default="", type=str)
        parser.add_argument('--last_name', required=False, default="", type=str)
        parser.add_argument('--email', required=False, default="", type=str)

        parser.add_argument('--is_active', required=False, action='store_true', default=True)
        parser.add_argument('--is_staff', required=False, action='store_true', default=False)
        parser.add_argument('--is_superuser', required=False, action='store_true', default=False)

        parser.add_argument('--channels', nargs='+', required=False, default=list(), type=str)
        parser.add_argument('--groups', nargs='+', required=False, default=list(), type=str)
        parser.add_argument('--permissions', nargs='+', required=False, default=list(), type=str)


    def handle(self, *args, **options):

        user = {
            'id': options['id'],
            'first_name': options['first_name'],
            'last_name': options['last_name'],
            'username': options['username'],
            'email': options['email'],
            'is_active': options['is_active'],
            'is_staff': options['is_staff'],
            'is_superuser': options['is_superuser'],
            'channels': options['channels'],
            'groups': options['groups'],
            'permissions': options['permissions'],
            getattr(settings, 'EXPIRATION_DATE_FIELD', 'exp'): int(options['expiration_date'].timestamp())
        }

        token = JWTAuth.encode_token(user).decode("utf-8")

        self.stdout.write(self.style.SUCCESS(token))
