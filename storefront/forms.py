from django import forms

class Itemform(forms.Form):
    item_id = forms.IntegerField(label="Item ID")
    item_name = forms.CharField(label="Name" ,max_length=200)
    item_price = form.IntegerField(label="Price")
    item_is_available = form.BooleanField(True)
