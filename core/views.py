from django.shortcuts import render
from django.db.models import Sum, FloatField, F
from django.utils import timezone
from .models import Sales


def home(request):
    qs = Sales.objects.all()
    qs_count = qs.values('id').annotate(
        amount=Sum(F('price', ) *
                   F('qty'), output_field=FloatField())).filter(date__gte=timezone.now).order_by("-id")

    total = 0
    for item in qs_count:
        total += item['amount']

    context = {
        "Sales": qs,
        "Total": total,
    }
    return render(request, "core/home.html", context=context)