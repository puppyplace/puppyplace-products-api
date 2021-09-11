from uuid import uuid4

from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f'{self.name}'