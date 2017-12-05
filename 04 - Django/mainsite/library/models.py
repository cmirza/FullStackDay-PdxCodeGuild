from django.db import models


class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateField()
    checked_out = models.BooleanField()

    def __str__(self):
        return f'{self.title} - {self.author}'
