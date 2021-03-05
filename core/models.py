from datetime import datetime
from django.db import models

from django.utils import translation
from django.utils.translation import ugettext as _


class Sales(models.Model):
    date = models.DateField(auto_now=True)
    day = models.CharField(max_length=200,
                           editable=True,
                           blank=True,
                           null=True)
    item_name = models.CharField(max_length=254, verbose_name="اسم المنتج")
    qty = models.PositiveSmallIntegerField(verbose_name="الكمية")
    price = models.DecimalField(verbose_name="السعر",
                                max_digits=10,
                                decimal_places=2)
    notes = models.CharField(max_length=254,
                             null=True,
                             blank=True,
                             verbose_name="ملاحظات")

    def __str__(self):
        return self.item_name + " | " + str(self.qty * self.price)


def pre_Sales_save_receiver(sender, instance, **kwargs):
    translation.activate('ar')
    if not instance.day:
        instance.day = _(date_format(datetime.today(), 'l'))