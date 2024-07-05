from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("humito_site.urls")),
    path("admin/", admin.site.urls),
]

