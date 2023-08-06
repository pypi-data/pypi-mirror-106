import jwt
from jwt import PyJWTError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from drfjwtauth.settings import ALGORITHM, SIGNING_KEY, AUTH_HEADER, EXPIRATION_DATE_FIELD, QUERY_PARAM_NAME
from drfjwtauth.user import JWTUser


class JWTAuth(BaseAuthentication):

    @classmethod
    def encode_token(cls, payload):
        return jwt.encode(payload, SIGNING_KEY, algorithm=ALGORITHM)

    @classmethod
    def decode_token(cls, encoded_token):
        return jwt.decode(encoded_token, SIGNING_KEY, algorithms=ALGORITHM)

    @classmethod
    def get_token_from_query_params(cls, request):
        return request.query_params.get(QUERY_PARAM_NAME)

    @classmethod
    def get_token_from_auth_header(cls, request):
        token = None
        header_value = request.META.get('HTTP_AUTHORIZATION')
        if header_value:
            if AUTH_HEADER not in header_value:
                pass  # TODO: launch error
            parts = header_value.split(AUTH_HEADER)
            token = parts[1].strip()
        return token

    @classmethod
    def get_token_from_request(cls, request):
        encoded_token = cls.get_token_from_query_params(request)
        if not encoded_token:
            encoded_token = cls.get_token_from_auth_header(request)
    
        return encoded_token

    def authenticate(self, request):
        user = None
        encoded_token = self.get_token_from_request(request)

        if encoded_token:
            try:
                data = self.decode_token(encoded_token)
            except PyJWTError as e:
                error = str(e)
                raise AuthenticationFailed(f'Invalid token: {error}')
            user = JWTUser(data, token=encoded_token)
        return user, None
