from uuid import uuid4

from django.db import models
from django.db.models.deletion import CASCADE

from apps.categories.models import Category


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    avatar_url = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    partner = models.UUIDField(null=True)

    def __str__(self):
        return f'{self.description}'
