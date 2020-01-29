from django.db import models

# Create your models here.
class ProductInfo(models.Model):

    product_id = models.CharField(max_length=10, primary_key=True)
    product_name = models.CharField(max_length=25)

     # Idenitfy self
    def __str__(self):
        return self.product_name

class ProductOptions(models.Model):
    option_id = models.CharField(max_length=25)
    option_name = models.CharField(max_length=25)
    product_id = models.CharField(max_length=25)
    unit_price = models.CharField(max_length=25)

    def __str__(self):
        return self.option_name

class TrsNatte(models.Model):
    trs_hieght = models.CharField(max_length=25)
    trs_24 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_28 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_32 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_36 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_40 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_44 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_48 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_52 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_56 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_60 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_64 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_68 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_72 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_76 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_80 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_84 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_88 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_92 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_96 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_100 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_104 = models.DecimalField(max_digits=6, decimal_places=2)
    trs_108 = models.DecimalField(max_digits=6, decimal_places=2)

    #def __str__(self):
        #return self.trs_24