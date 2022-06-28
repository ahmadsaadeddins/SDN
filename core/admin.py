from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Sales, Expenses, Inventory, Purchase, Item_Card


class SalesResource(resources.ModelResource):
    class Meta:
        model = Sales


class SalesAdmin(ImportExportModelAdmin):
    resource_class = SalesResource


admin.site.register(Sales, SalesAdmin)


class ExpensesResource(resources.ModelResource):
    class Meta:
        model = Expenses


class ExpensesAdmin(ImportExportModelAdmin):
    resource_class = ExpensesResource


admin.site.register(Expenses, ExpensesAdmin)


class Item_CardResource(resources.ModelResource):
    class Meta:
        model = Item_Card


class Item_CardAdmin(ImportExportModelAdmin):
    resource_class = Item_CardResource


admin.site.register(Item_Card, Item_CardAdmin)


class InventoryResource(resources.ModelResource):
    class Meta:
        model = Inventory


class InventoryAdmin(ImportExportModelAdmin):
    resource_class = InventoryResource


admin.site.register(Inventory, InventoryAdmin)


class PurchaseResource(resources.ModelResource):
    class Meta:
        model = Purchase


class PurchaseAdmin(ImportExportModelAdmin):
    resource_class = PurchaseResource


admin.site.register(Purchase, PurchaseAdmin)
