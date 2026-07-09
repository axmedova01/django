import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from django.conf import settings

class JWTAuthenticationClass(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('access_token')

        if not token:
            raise AuthenticationFailed('Требуется токен для доступа к защищенному ресурсу')



        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Срок действия токена истек')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Недействительный токен')

        # Извлеките и проверьте роли пользователя из токена
        user_roles = payload.get('roles', [])
        request.user_roles = user_roles

        user = User.objects.get(username=payload['username'])
        return user, token



