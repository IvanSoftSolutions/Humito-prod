from django.http import HttpResponse
from django.shortcuts import render
from .models import VapeInfo

def index(request):
    item_list = VapeInfo.objects.order_by("id")
    context = {
        "item_list": item_list,
    }
    return render(request, "website/index.html", context)


def detail(request, item_id):
    item = VapeInfo.objects.get(id=item_id)
    return render(request, "website/detail.html", {"item": item})