from django.urls import path
from .views import LoginView, ProtectedResourceView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedResourceView.as_view(), name='protected_resource'),
    path('protected/<int:pk>/', ProtectedResourceView.as_view(), name='protected_resource_detail'),
]
