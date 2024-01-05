
from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static




schema_view = get_schema_view(
    openapi.Info(
        title="API Transaction",
        default_version='v1',
        description="Эта API создана для преобразования текста в речь",
        terms_of_service="http://itcbootcamp.com",
        contact=openapi.Contact(
            name = "Xeniya",
            url = "https://t.me/Xeniyakot",
            email="xeniasolovyovakot@yandex.kz",
            ),
        license=openapi.License(
            name="BSD License"
            ),
        ), 
    public = True,
    permission_classes = [permissions.AllowAny,] 
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )