from django.db import models

# Create your models here.

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    owner = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    item_name = models.CharField(max_length=128)
    min_bid = models.IntegerField()
    auto_buy = models.IntegerField()

class Transaction(models.Model):
    location = models.CharField(max_length=128)
    pickup_date = models.DateField()
    return_date = models.DateField()
    item_id = models.ForeignKey(Item, on_delete= models.CASCADE)

class Bid(models.Model):
    BID_STATUS = (
        ('PENDING', 'PENDING'),
        ('REJECTED', 'REJECTED'),
        ('ACCEPTED', 'ACCEPTED'),
    )
    bidding_status = models.CharField(max_length=8, choices=BID_STATUS, default='REJECTED')
    bidding_price = models.IntegerField(default=0)
    bidder_name = models.CharField(primary_key=True,max_length=64)
    tid = models.IntegerField()

    class Meta:
        unique_together = (("bidder_name", "tid"),)
