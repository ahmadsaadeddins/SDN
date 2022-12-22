from django.db import models
from django.db.models.signals import post_save, pre_save, pre_init
from django.dispatch import receiver

# Create your models here.


class Inventory(models.Model):
    name_inventory = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name_inventory


class Tools(models.Model):
    name_tool = models.CharField(max_length=100, null=True)
    mac_tool = models.CharField(max_length=100, null=True)
    ip_tool = models.CharField(max_length=100, null=True)
    ssid_tool = models.CharField(max_length=100, null=True)
    model_tool = models.CharField(max_length=100, null=True)
    inventory_tool = models.ForeignKey(Inventory,
                                       on_delete=models.SET_NULL,
                                       null=True)
    state = models.CharField(max_length=100, null=True)
    tower = models.ForeignKey('Towers', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} {}".format(self.name_tool, self.model_tool)


class Towers(models.Model):
    name_tower = models.CharField(max_length=100)
    location_tower = models.CharField(max_length=100)
    notes = models.TextField(null=True)

    #tools_tower = models.ForeignKey(Tools, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name_tower


class Customers(models.Model):
    name_customer = models.CharField(max_length=100)
    tools_customer = models.ManyToManyField(Tools)


# @receiver(post_save, sender=Towers)
# def removeFromlInv(sender, instance, *args, **kwargs):
#     tools = Tools.objects.all()
#     # print(instance.tools_tower.all()[0].name_tool)
#     for tool in instance.tools_tower.all():
#         for t in tools:
#             print(t == tool)
#             if t == tool:
#                 t.state = "tower {}".format(instance.name_tower)
#                 t.save()
#             else:
#                 t.state = ""
#                 t.save()
# print("you save something {}".format(instance.name_customer))
