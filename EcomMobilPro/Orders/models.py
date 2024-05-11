from django.db import models
from Customers.models import Customer
from Products.models import product


class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = (
        (ORDER_DELIVERED, "Order delivered"),
        (ORDER_CONFIRMED, "Order confirmed"),
        (ORDER_PROCESSED, "Order processde"),
        (ORDER_REJECTED, "Order rejected")
    )
    
    order_status = models.IntegerField(choices= STATUS_CHOICE, default=CART_STAGE)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='order', null=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.pr_name


class orderItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL, related_name="add_cart", null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')