from django.urls import path

from apps.example_api.api.v1 import views

urlpatterns = [
    path('categories/', views.all_categories, name='all_categories'),
]
