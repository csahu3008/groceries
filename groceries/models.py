from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class GroceryItem(models.Model):
    title=models.CharField(_("Title"),max_length=100)
    description=models.CharField(_("Description"),max_length=2000)
    createdAt=models.DateTimeField(_("Created At"),auto_now_add=True,auto_now=False)
    price=models.BigIntegerField(_("Price"))
