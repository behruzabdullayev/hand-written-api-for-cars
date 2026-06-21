from django.urls import path
from .views import CarListAPIView, CarCreateAPIView, CarDetailAPIView, CarUpdateAPIView, CarDeleteAPIView, CarDetailUpdateAPIView, CarListCreateAPIView

urlpatterns = [
    path('cars/', CarListAPIView.as_view()),
    path('cars/create/', CarCreateAPIView.as_view()),
    path('cars/<int:pk>/detail/', CarDetailAPIView.as_view()),
    path('cars/<int:pk>/update/', CarUpdateAPIView.as_view()),
    path('cars/<int:pk>/delete/', CarDeleteAPIView.as_view()),
    path('cars/<int:pk>/detail/update/', CarDetailUpdateAPIView.as_view()),
    path('cars/list/create/', CarListCreateAPIView.as_view()),
]