from django.urls import path

from apps.example_api.api.v1 import views

urlpatterns = [
    path('v1/', views.index, name='index'),
]
