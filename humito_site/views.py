from django.http import HttpResponse
from django.shortcuts import render
from .models import VapeInfo, VapeImages

def index(request):
    item_list = VapeInfo.objects.order_by("id")
    context = {
        "item_list": item_list,
    }
    return render(request, "humito_site/index.html", context)


def detail(request, item_id):
    item = VapeInfo.objects.get(id=item_id)
    image_list = VapeImages.objects.filter(vape_id_id=item_id)
    context = {
        "item": item,
        "image_list": image_list
    }
    return render(request, "humito_site/detail.html", context)

def filter_disponible(request):
    item_list = VapeInfo.objects.filter(available=True)
    context = {
        "item_list": item_list,
    }
    return render(request, "humito_site/index.html", context)

def filter_pedido(request):
    item_list = VapeInfo.objects.filter(available=False)
    context = {
        "item_list": item_list,
    }
    return render(request, "humito_site/index.html", context)