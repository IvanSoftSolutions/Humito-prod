from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:item_id>/", views.detail, name="detail"),
    path("disponible", views.filter_disponible, name="available"),
    path("solo_pedido", views.filter_pedido, name="on_demand"),
]