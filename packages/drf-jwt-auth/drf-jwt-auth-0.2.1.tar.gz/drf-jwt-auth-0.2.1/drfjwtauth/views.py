from jwt import PyJWTError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drfjwtauth.auth import JWTAuth


class VerifyJWTView(APIView):

    def post(self, request):
        token = request.data.get('token') or JWTAuth.get_token_from_request(request)

        # Accept JWT as token parameter in the body and in the Authorization header as 
        # authentication class does.
        if not token:
            return Response({
                'error': 'Missing JWT in the received request. Set it in the body or in the Authentication header'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            JWTAuth.decode_token(token)
        except PyJWTError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'ok'})
