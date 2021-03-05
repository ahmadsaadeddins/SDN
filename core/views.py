from django.shortcuts import render
from .models import Sales


def home(request):
    qs = Sales.objects.all()
    context = {"Sales": qs}
    return render(request, "core/home.html", context=context)