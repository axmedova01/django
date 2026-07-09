from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
import jwt
from django.conf import settings

class LoginView(APIView):
    @authentication_classes([])
    @permission_classes([])
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token = AccessToken.for_user(user)
            return Response({'access_token': str(token),
                             'http': 'http://127.0.0.1:8000/protected_resource/?access_token='+str(token)
                             })
        else:
            raise AuthenticationFailed('Неверный логин или пароль')


class ProtectedResourceView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, request):
        token = request.query_params.get('access_token')

        if not token:
            raise AuthenticationFailed('Требуется токен для доступа к защищенному ресурсу')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Срок действия токена истек')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Недействительный токен')

        return Response({'message': 'У вас есть доступ к защищенному ресурсу'})


def index(request):
    return render(request, 'main/index.html')