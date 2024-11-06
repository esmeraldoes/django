from django.db import models

class Book(models.Model):
    title = models.CharField("Title", max_length=200)
    author = models.CharField("Author", max_length=200)
    genre = models.CharField("Genre", max_length=100)
    publication_year = models.PositiveIntegerField("Publication Year")

    class Meta:
        ordering = ['-publication_year']
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} by {self.author}"
