from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    # Administración y autorizacion de la api
    path('admin/', admin.site.urls, name='admin'),
    path('docs/', include_docs_urls(title='GesSAI API')),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    re_path(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # Rutas de la API
    path('gessaiapi/v1/', include('config.router'), name='base_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
