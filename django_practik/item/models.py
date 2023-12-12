from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)
    psevdonim = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return f'{self.name} -> {self.date_of_birth} '
    

class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    title = models.CharField(max_length=60)
    created_at = models.DateField()
    genre = models.CharField(max_length=5)
    