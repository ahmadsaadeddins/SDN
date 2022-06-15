from datetime import datetime
from decimal import Decimal

from django.db import models
from django.db.models import Avg, Max, Sum
from django.db.models.signals import pre_save, post_save, pre_delete

from django.utils import translation
from django.utils.formats import date_format
from django.utils.translation import gettext_lazy as _


class Item_Card(models.Model):
    item_name = models.CharField(max_length=254, verbose_name="اسم المنتج")

    def __str__(self):
        return self.item_name


class Purchase(models.Model):
    date = models.DateField(auto_now=True)
    day = models.CharField(max_length=200,
                           editable=True,
                           blank=True,
                           null=True)
    item_name = models.ForeignKey(Item_Card,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  verbose_name="اسم المنتج")
    qty = models.PositiveSmallIntegerField(verbose_name="الكمية")
    Purchase_price = models.DecimalField(verbose_name="سعر الشراء",
                                         max_digits=10,
                                         decimal_places=2)
    selling_price = models.DecimalField(verbose_name="سعر البيع",
                                        max_digits=10,
                                        decimal_places=2)
    wholesale_price = models.DecimalField(verbose_name=" سعر بيع الجمله",
                                          max_digits=10,
                                          decimal_places=2)
    notes = models.CharField(max_length=254,
                             null=True,
                             blank=True,
                             verbose_name="ملاحظات")

    class Meta:
        verbose_name = "المشتريات"
        verbose_name_plural = "المشتريات"

    def __str__(self):
        return self.item_name.item_name + " | " + str(
            self.qty * self.selling_price)


class Sales(models.Model):
    date = models.DateField(auto_now=True)
    day = models.CharField(max_length=200,
                           editable=True,
                           blank=True,
                           null=True)
    item_name = models.ForeignKey(Item_Card,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  verbose_name="اسم المنتج")
    qty = models.PositiveSmallIntegerField(verbose_name="الكمية")
    selling_price = models.DecimalField(verbose_name="سعر البيع",
                                        max_digits=10,
                                        decimal_places=2)

    notes = models.CharField(max_length=254,
                             null=True,
                             blank=True,
                             verbose_name="ملاحظات")

    class Meta:
        verbose_name = "المبيعات"
        verbose_name_plural = "المبيعات"

    def __str__(self):
        return self.item_name.item_name + " | " + str(
            self.qty * self.selling_price)


class Inventory(models.Model):
    date = models.DateField(auto_now=True)
    item_name = models.ForeignKey(Item_Card,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  verbose_name="اسم المنتج")
    qty = models.PositiveSmallIntegerField(verbose_name="الكمية")
    wholesale_price = models.DecimalField(verbose_name=" سعر بيع الجمله",
                                          max_digits=10,
                                          decimal_places=2)

    class Meta:
        verbose_name = "المخزن"
        verbose_name_plural = "المخزن"

    def __str__(self):
        return self.item_name.item_name + " | " + str(self.qty)


class Expenses(models.Model):
    date = models.DateField(auto_now=True)
    expense_name = models.CharField(max_length=254, verbose_name="اسم المصروف")
    qty = models.PositiveSmallIntegerField(verbose_name="الكمية")
    price = models.DecimalField(verbose_name="السعر",
                                max_digits=10,
                                decimal_places=2)
    notes = models.CharField(max_length=254,
                             null=True,
                             blank=True,
                             verbose_name="ملاحظات")

    class Meta:
        verbose_name = "المصاريف"
        verbose_name_plural = "المصاريف"

    def __str__(self):
        return self.expense_name + " | " + str(self.qty * self.price)


def post_inventory_save_receiver(sender, instance, created, **kwargs):
    print("post_inventory_save_receiver")
    print(created)
    if created:
        avg_item_price = Purchase.objects.filter(
            item_name=instance.item_name).aggregate(
                Avg('wholesale_price'))['wholesale_price__avg']
        check_item_in_inventory = Inventory.objects.filter(
            item_name=instance.item_name)
        if check_item_in_inventory:
            inv_item = Inventory.objects.get_or_create(
                item_name=instance.item_name)
            inv_item[0].wholesale_price = avg_item_price
            inv_item[0].qty += instance.qty
            inv_item[0].save()
        else:
            inv_item = Inventory.objects.get_or_create(
                item_name=instance.item_name,
                qty=instance.qty,
                wholesale_price=instance.wholesale_price)
    else:
        avg_item_price = Purchase.objects.filter(
            item_name=instance.item_name).aggregate(
                Avg('wholesale_price'))['wholesale_price__avg']
        check_item_in_inventory = Inventory.objects.filter(
            item_name=instance.item_name)
        if check_item_in_inventory:
            inv_item = Inventory.objects.get_or_create(
                item_name=instance.item_name)
            inv_item[0].wholesale_price = avg_item_price
            inv_item[0].qty += instance.qty
            inv_item[0].save()
        else:
            inv_item = Inventory.objects.get_or_create(
                item_name=instance.item_name,
                qty=instance.qty,
                wholesale_price=instance.wholesale_price)


def pre_purchase_save_receiver(sender, instance, **kwargs):
    translation.activate('ar')
    if not instance.day:
        instance.day = _(date_format(datetime.today(), 'l'))


def pre_sales_save_receiver(sender, instance, **kwargs):
    translation.activate('ar')
    if not instance.day:
        instance.day = _(date_format(datetime.today(), 'l'))
    sum_item_qty = Purchase.objects.filter(
        item_name=instance.item_name).aggregate(Sum('qty'))['qty__sum']
    avg_item_price = Purchase.objects.filter(
        item_name=instance.item_name).aggregate(
            Avg('wholesale_price'))['wholesale_price__avg']
    if sum_item_qty and instance.selling_price >= avg_item_price:
        inv_item = Inventory.objects.get_or_create(
            item_name=instance.item_name)
        inv_item[0].qty -= instance.qty
        inv_item[0].save()
    else:
        print("error")


def pre_sales_delete_receiver(sender, instance, **kwargs):
    inv_item = Inventory.objects.get_or_create(item_name=instance.item_name)
    inv_item[0].qty += instance.qty
    inv_item[0].save()


def pre_purchase_delete_receiver(sender, instance, **kwargs):
    inv_item = Inventory.objects.get_or_create(item_name=instance.item_name)
    inv_item[0].qty -= instance.qty
    inv_item[0].save()


post_save.connect(post_inventory_save_receiver, sender=Purchase)
pre_save.connect(pre_purchase_save_receiver, sender=Purchase)
pre_save.connect(pre_sales_save_receiver, sender=Sales)
pre_delete.connect(pre_sales_delete_receiver, sender=Sales)
pre_delete.connect(pre_purchase_delete_receiver, sender=Purchase)
