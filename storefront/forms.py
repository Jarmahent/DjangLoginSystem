from django import forms
from storefront.models import storeItem

class Itemform(forms.ModelForm):
    item_name = forms.CharField(label="Item Name" ,max_length=200)
    item_description = forms.CharField(label="Item Description" ,max_length=500, widget=forms.Textarea)
    item_price = forms.DecimalField(label="Item Price", max_value=500, decimal_places=3)
    item_is_available = forms.TypedChoiceField(choices=((False, 'No'), (True, 'Yes')))
    item_image = forms.FileField(label="Item Image", required=True)


class ItemModelForm(Itemform):
    class Meta:
        model = storeItem
        field = ['item_name', 'item_price', 'item_is_available', 'item_description', 'item_image']
        exclude = ['item_id']
