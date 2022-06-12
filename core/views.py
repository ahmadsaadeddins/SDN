from django.shortcuts import render
from django.db.models import Sum, FloatField, F
from django.utils import timezone
from .models import Sales, Expenses


def home(request):
    qs = Sales.objects.all().filter(date__gte=timezone.now()).order_by("-id")
    qs_count = qs.values('id').annotate(
        amount=Sum(F('Purchase_price', ) *
                   F('qty'), output_field=FloatField())).order_by("-id")

    total = 0
    for item in qs_count:
        total += item['amount']

    context = {
        "Sales": qs,
        "Total": total,
    }
    return render(request, "core/home.html", context=context)


def total(request):
    qs = Sales.objects.all().order_by("-id")
    qs_count = qs.values('id').annotate(
        amount=Sum(F('selling_price', ) *
                   F('qty'), output_field=FloatField())).order_by("-id")

    total = 0
    for item in qs_count:
        total += item['amount']

    context = {
        "Sales": qs,
        "Total": total,
    }
    return render(request, "core/home.html", context=context)


def total_expenses(request):
    qs = Expenses.objects.all().order_by("-id")
    qs_count = qs.values('id').annotate(
        amount=Sum(F('selling_price', ) *
                   F('qty'), output_field=FloatField())).order_by("-id")

    total = 0
    for item in qs_count:
        total += item['amount']

    context = {
        "Sales": qs,
        "Total": total,
    }
    return render(request, "core/home.html", context=context)