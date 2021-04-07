from django.urls import path
from . import views as coreViews

app_name = 'core'
urlpatterns = [
    path('', coreViews.home, name='home'),
    path('total/', coreViews.total, name='total'),
    path('totale/', coreViews.total_expenses, name='total-expenses'),
]