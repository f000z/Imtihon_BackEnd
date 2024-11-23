from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create the schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="This is the API documentation for the furniture shop project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('registration/', include('account.urls')),  # Registration route (with trailing slash)
] + i18n_patterns(  # Internationalization patterns
    path('i18n/', include('django.conf.urls.i18n')),  # Path for handling translations
    path('', include('shop.urls')),  # Shop URLs for homepage, products, etc.
)

# Swagger URL
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Static and media file handling in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


