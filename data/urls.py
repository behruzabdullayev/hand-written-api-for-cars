from django.urls import path
from .views import CarListAPIView, CarCreateAPIView, CarDetailAPIView, CarUpdateAPIView, CarDeleteAPIView, CarDetailUpdateAPIView, CarListCreateAPIView
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('cars/', CarListAPIView.as_view()),
    path('cars/create/', CarCreateAPIView.as_view()),
    path('cars/<int:pk>/detail/', CarDetailAPIView.as_view()),
    path('cars/<int:pk>/update/', CarUpdateAPIView.as_view()),
    path('cars/<int:pk>/delete/', CarDeleteAPIView.as_view()),
    path('cars/<int:pk>/detail/update/', CarDetailUpdateAPIView.as_view()),
    path('cars/list/create/', CarListCreateAPIView.as_view()),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]