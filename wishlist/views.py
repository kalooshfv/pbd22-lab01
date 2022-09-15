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
    return render(request, "wishlist.html", context)

def show_xml(request):
    data = ItemWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), \
        content_type="application/xml")

def show_json(request):
    data = ItemWishlist.objects.all() 
    return HttpResponse(serializers.serialize("json", data), \
        content_type="application/json")

def show_json_by_id(request, id):
    data = data = ItemWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), \
        content_type="application/json")

def show_xml_by_id(request, id):
    data = data = ItemWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), \
        content_type="application/xml")
