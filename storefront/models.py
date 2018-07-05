from django.db import models

# Create your models here.


class store_item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_is_available = models.BooleanField(default=True)
    item_description = models.CharField(max_length=500)

    def __str__(self):
        return self.item_name
