from django.contrib import admin
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
from .models import Sales, Expenses, Inventory, Purchase, Item_Card

# class SalesResource(resources.ModelResource):
#     class Meta:
#         model = Sales

# class SalesAdmin(ImportExportModelAdmin):
#     resource_class = SalesResource

# admin.site.register(Sales, SalesAdmin)

# class ExpensesResource(resources.ModelResource):
#     class Meta:
#         model = Expenses

# class ExpensesAdmin(ImportExportModelAdmin):
#     resource_class = ExpensesResource

# admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Item_Card)
admin.site.register(Inventory)
admin.site.register(Purchase)
admin.site.register(Expenses)
admin.site.register(Sales)
# Register your models here.
# admin.site.register(SalesResource, Expenses)