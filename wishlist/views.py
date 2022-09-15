from django.shortcuts import render
from wishlist.models import ItemWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_wishlist_item = ItemWishlist.objects.all()
    context = {
        'list_item': data_wishlist_item,
        'name': 'Kaloosh Falito Verrell'
    }
    return HttpResponse(serializers.serialize("xml", data_wishlist_item), \
        content_type="application/xml")