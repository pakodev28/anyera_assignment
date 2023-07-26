from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import PetViewSet, UserPetsViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r"pets", PetViewSet)
router.register(r"users", UserPetsViewSet, basename="user")

urlpatterns = [
    path(
        "register/", UserRegistrationView.as_view(), name="user-registration"
    ),
    path("login/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("", include(router.urls)),
]
