from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} -> {self.price} '

class Item2(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='items'
    )