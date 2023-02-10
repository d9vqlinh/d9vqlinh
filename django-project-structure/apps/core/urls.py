from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Pastebin API')
app_name = "core"

urlpatterns = [
    path('', include('apps.example_api.urls')),
    # path(r'^$', schema_view)
]
