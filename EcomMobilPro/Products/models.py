from django.db import models

# brands Model

class brand(models.Model):
    Brand_name = models.CharField(max_length=100)
    Brand_logo = models.ImageField(upload_to='media', null=True)
    
    def __str__(self):
        return self.Brand_name
    
    
# Mobiles model
    
class product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'live'), (DELETE, 'delete'))
    pr_name = models.CharField(max_length=200)
    Brand_name = models.ForeignKey(brand, on_delete= models.CASCADE, related_name='product_brand')
    pr_price = models.DecimalField(max_digits=15, decimal_places=2)
    pr_Description = models.TextField()
    pr_image = models.ImageField(upload_to= 'media')
    Priority = models.IntegerField(default= 0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.pr_name