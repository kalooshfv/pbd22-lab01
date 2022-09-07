from django.db import models

# Create your models here.
class ItemWishlist(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    description = models.TextField()