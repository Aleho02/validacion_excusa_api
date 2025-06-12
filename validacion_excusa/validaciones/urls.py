from django.urls import path
from .views import (
    ValidacionListCreateAPIView,
    ValidacionRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('validaciones/', ValidacionListCreateAPIView.as_view(), name='validacion-list-create'),
    path('validaciones/<int:pk>/', ValidacionRetrieveUpdateDestroyAPIView.as_view(), name='validacion-detail'),
]
