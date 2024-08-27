from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserDeleteView,
    UserListView,
    UserRetrieveView,
    UserUpdateView,
    PaymentCreateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="user-register"),
    path("detail/<int:pk>/", UserRetrieveView.as_view(), name="user-detail"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
    path("users_list/", UserListView.as_view(), name="users-list"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token-refresh",
    ),
    path("payment/", PaymentCreateAPIView.as_view(), name="payment-list"),
]
