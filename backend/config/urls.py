# backend/config/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.renderers import JSONRenderer

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from projects.views import ProjectViewSet
from vacancy.views import VacancyViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'vacancies', VacancyViewSet, basename='vacancy')


urlpatterns = [

    path('admin/', admin.site.urls),


    path('api/', include(router.urls)),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),


    path(
        'api/schema.json',
        SpectacularAPIView.as_view(renderer_classes=[JSONRenderer]),
        name='schema-json'
    ),


    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),


    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
