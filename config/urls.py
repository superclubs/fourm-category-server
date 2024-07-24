from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from config._admin.admin import custom_admin_site
from config.docs import schema_view
from config.redirects import redirect_swagger_view

admin.site.site_header = "FORUM CATEGORY"
admin.site.site_title = "FORUM CATEGORY"
admin.site.index_title = "포럼 카테고리 관리자 페이지"

urlpatterns = (
    [
        path("", redirect_swagger_view),
        # Admin
        path("jet/", include("jet.urls", "jet")),
        # path(settings.ADMIN_URL, admin.site.urls),
        path(settings.ADMIN_URL, custom_admin_site.urls),
        # Allauth
        path("accounts/", include("allauth.urls")),
        # Advanced Filters
        path("advanced_filters/", include("advanced_filters.urls")),
        # DRF auth token
        path("auth-token/", obtain_auth_token),
        # django-health-check
        path("ht/", include("health_check.urls")),
        # summernote
        path("summernote/", include("django_summernote.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

# API URLS
urlpatterns += [
    # API base url
    path("api/", redirect_swagger_view),
    path("api/v1/", include("config.api_router")),
    # JWT
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Swagger
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
