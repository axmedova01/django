from django.urls import path
from . import views
from .views import ProtectedResourceView, LoginView


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected_resource/', ProtectedResourceView.as_view(), name='protected_resource'),
]