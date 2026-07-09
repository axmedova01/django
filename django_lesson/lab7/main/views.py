from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Token, Good
from .serializers import GoodSerializer

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    token = Token.objects.create()
    return Response({'token': str(token.token)})

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def goods(request):
    token = request.GET.get('token')
    if not token:
        return Response('Token must be present', status=401)
    try:
        token_obj = Token.objects.get(token=token)
    except Token.DoesNotExist:
        return Response('Token is invalid', status=401)
    goods = Good.objects.all()
    serializer = GoodSerializer(goods, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def new_good(request):
    token = request.GET.get('token')
    if not token:
        return Response('Token must be present', status=401)
    try:
        token_obj = Token.objects.get(token=token)
    except Token.DoesNotExist:
        return Response('Token is invalid', status=401)
    serializer = GoodSerializer(data=request.data)
    if serializer.is_valid():
        amount = serializer.validated_data.get('amount')
        price = serializer.validated_data.get('price')
        if amount < 0 or price < 0:
            return Response('Amount and price are negative', status=400)
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)