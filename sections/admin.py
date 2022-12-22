from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from nested_admin import NestedModelAdmin, NestedTabularInline
# Register your models here.


class ToolsInlineTower(NestedTabularInline):
    model = Tools
    extra = 0
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':50})},
    # }


# class ToolsInlineTower(admin.StackedInline):
#     model = Tools
#     extra = 1


class ToolsInlineCustomer(admin.TabularInline):
    model = Customers.tools_customer.through


class customerAdmin(admin.ModelAdmin):
    fields = ('name_customer', 'tools_customer')
    list_display = ('name_customer', 'ToolsCustomers')

    def ToolsCustomers(self, obj):
        data = [Tools.name_tool for Tools in obj.tools_customer.all()]
        return '{}'.format(len(data))

    list_filter = ['name_customer']
    search_fields = ['name_customer']
    inlines = [ToolsInlineCustomer]


class TowersAdmin(NestedModelAdmin):
    fields = (
        'name_tower',
        'location_tower',
        'notes',
    )
    list_display = ('name_tower', 'location_tower')

    # def ToolsTower(self, obj):
    #     data = [
    #         f"{tool.name_tool}-{tool.mac_tool}"
    #         for tool in obj.tools_tower.all()
    #     ]
    #     aa = obj.tools_tower.count()
    #     return aa

    list_filter = ('name_tower', 'location_tower')
    search_fields = ('name_tower', 'location_tower')
    inlines = [ToolsInlineTower]


class ToolsAdmin(admin.ModelAdmin):
    fields = ('name_tool', 'mac_tool', 'ip_tool', 'ssid_tool', 'model_tool',
              'inventory_tool', 'tower')
    list_display = ('name_tool', 'mac_tool', 'ip_tool', 'ssid_tool',
                    'model_tool', 'inventory_tool', 'state')
    list_editable = ('ssid_tool', 'inventory_tool')
    list_filter = ('model_tool', 'inventory_tool')
    search_fields = ('name_tool', 'ip_tool', 'mac_tool')


admin.site.register(Inventory)
admin.site.register(Towers, TowersAdmin)
admin.site.register(Tools, ToolsAdmin)
admin.site.register(Customers, customerAdmin)
