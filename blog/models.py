from django.db import models

class Product(models.Model):
    name_product = models.CharField(max_length=100)
    discriptions = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ important
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    def __str__(self):
        return f'{self.name_product} - {self.id} - {self.created_at}'
