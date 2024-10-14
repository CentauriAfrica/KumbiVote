"""
URL configuration for kumbivote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.elections.views import ElectionViewSet
from apps.organizations.views import OrganizationViewSet

# from apps.users.oauth2_views import (
#     TokenView,  # noqa
# )
from apps.users.views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"elections", ElectionViewSet)
router.register(r"organizations", OrganizationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(router.urls),
    ),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    #     path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    #     path("oauth2/userinfo", UserInfoView.as_view(), name="oauth2_userinfo"),
    #     path("oauth2/token", TokenView.as_view(), name="oauth2_token"),
    #     path(
    #         "oauth2/revoke_token/",
    #         RevokeTokenView.as_view(),
    #         name="oauth2_revoke_token",
    #     ),
]
