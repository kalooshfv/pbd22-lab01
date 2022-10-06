from django import forms
from wishlist.models import *

class WishlistForm(forms.ModelForm):
    class Meta:
        model = ItemWishlist
        fields = ['item_name', 'item_price', 'description']
        