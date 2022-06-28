from django import forms
from .models import Expenses, Item_Card, Purchase, Sales


class Item_CardForm(forms.ModelForm):
    class Meta:
        model = Item_Card
        fields = ['item_name']


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ["expense_name", "qty", "price", "notes"]


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            "item_name", "qty", "Purchase_price", "selling_price",
            "wholesale_price", "notes"
        ]


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ["item_name", "qty", "selling_price", "notes"]