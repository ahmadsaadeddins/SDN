from django.urls import path
from . import views as coreViews

app_name = 'core'
urlpatterns = [
    path('', coreViews.home, name='home'),
    path('purchase/create/', coreViews.create_purchase,
         name="create-purchase"),
    path('expenses/create/', coreViews.create_expenses,
         name="create-expenses"),
    path('sales/create/', coreViews.create_sales, name="create-sales"),
    path('total/', coreViews.total, name='total'),
    path('totale/', coreViews.total_expenses, name='total-expenses'),
]