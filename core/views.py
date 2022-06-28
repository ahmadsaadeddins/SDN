from django.shortcuts import render, redirect
from django.db.models import Sum, FloatField, F
from django.utils import timezone
from .models import Sales, Expenses, Purchase, Item_Card
from .forms import SalesForm, ExpensesForm, PurchaseForm, Item_CardForm


def home(request):
    qs = Sales.objects.all().filter(date__gte=timezone.now()).order_by("-id")
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


def create_purchase(request):
    form = PurchaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context = {"form": form}
    return render(request, "core/form.html", context)


def create_sales(request):
    form = SalesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context = {"form": form}
    return render(request, "core/form.html", context)


def create_expenses(request):
    form = ExpensesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")

    context = {"form": form}
    return render(request, "core/form.html", context)