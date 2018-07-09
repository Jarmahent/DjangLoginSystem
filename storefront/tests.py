from django.test import TestCase
from storefront.models import storeItem
# Create your tests here.

item = storeItem(item_name="Shoe", item_price=22, item_is_available=True, item_description="desc", item_image="media")
item.save()


# items = storeItem.objects.values()
#
