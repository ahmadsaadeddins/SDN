from django.db import models


class Sales(models.Model):
    item_name = models.CharField(max_length=254, verbose_name="اسم المنتج")
    qty = models.PositiveSmallIntegerField(verbose_name="الكمية")
    price = models.DecimalField(verbose_name="السعر",
                                max_digits=10,
                                decimal_places=2)
    notes = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.item_name + " | " + str(qty * price)