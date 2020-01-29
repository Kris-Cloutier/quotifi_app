import uuid
from django.db import models

# Create your models here.
class Order(models.Model):

    customer_id = models.CharField(max_length=25)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    quantity = models.CharField(max_length=25)
    room_location = models.CharField(max_length=25)
    width = models.CharField(max_length=25)
    height = models.CharField(max_length=25)
    openess = models.CharField(max_length=25)
    product = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    frame = models.CharField(max_length=25)
    custom = models.CharField(max_length=25)
    angled_build_out = models.CharField(max_length=25)
    safety_drive = models.CharField(max_length=25)
    radio = models.CharField(max_length=25)
    remote = models.CharField(max_length=25)
    helper = models.CharField(max_length=25)
    extreme = models.CharField(max_length=25)
    vinyl_panel = models.CharField(max_length=25)
    mortar = models.CharField(max_length=25)
