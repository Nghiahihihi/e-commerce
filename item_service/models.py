# item_service/models.py

from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('book', 'Book'),
        ('electronic', 'Electronic'),
        ('general', 'General'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)

    image_url = models.URLField(null=True, blank=True)  # 👈 thêm dòng này

    def __str__(self):
        return f"{self.name} ({self.category})"
