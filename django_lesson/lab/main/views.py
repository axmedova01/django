from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import authentication_classes, permission_classes
from .authentication import JWTAuthenticationClass
from .models import Todo
from .serializers import TodoSerializer
import jwt
from django.conf import settings


@authentication_classes([])
@permission_classes([])
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            payload = dict(user_id=user.id, username=user.username)

            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            return Response({'access_token': str(token),
                             'http': 'http://127.0.0.1:8000/protected/?access_token=' + str(token)
                             })
        else:
            raise AuthenticationFailed('Неверный логин или пароль')




@authentication_classes([JWTAuthenticationClass])
@permission_classes([IsAuthenticated])
class ProtectedResourceView(APIView):
    def get(self, request, pk=None):
        user = request.user
        # Вывод конкретного запроса по id
        if pk is not None:
            try:
                todo = Todo.objects.get(id=pk)
                serializer = TodoSerializer(todo)
                return Response(serializer.data)
            except Todo.DoesNotExist:
                return Response({'message': 'Элемент с указанным ID не найден'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_superuser:
            queryset = Todo.objects.all()
        else:
            queryset = Todo.objects.filter()

        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user

        if user.has_perm('main.add_todo'):
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Данные успешно добавлены', 'data': serializer.data})
            else:
                return Response({'message': 'Ошибка валидации данных', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'У вас нет прав для выполнения этой операции'}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        user = request.user

        if user.has_perm('main.change_todo'):
            try:
                todo = Todo.objects.get(id=pk)
            except Todo.DoesNotExist:
                return Response({'message': 'Элемент с указанным ID не найден'}, status=status.HTTP_404_NOT_FOUND)

            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Данные успешно обновлены', 'data': serializer.data})
            else:
                return Response({'message': 'Ошибка валидации данных', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'У вас нет прав для выполнения этой операции'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        user = request.user

        if user.has_perm('main.delete_todo'):
            try:
                todo = Todo.objects.get(id=pk)
            except Todo.DoesNotExist:
                return Response({'message': 'Элемент с указанным ID не найден'}, status=status.HTTP_404_NOT_FOUND)

            todo.delete()
            return Response({'message': 'Данные успешно удалены'})
        else:
            return Response({'message': 'У вас нет прав для выполнения этой операции'}, status=status.HTTP_403_FORBIDDEN)
