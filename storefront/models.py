from django.db import models

# Create your models here.


class storeItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200, default="NoName")
    item_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    item_is_available = models.BooleanField(default=True)
    item_description = models.CharField(max_length=500, default="None")
    item_image = models.FileField(upload_to="", default='media')

    def __str__(self):
        return self.item_name
