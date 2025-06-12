from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, FuncionarioViewSet, register_user

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
]
