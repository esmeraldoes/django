from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SCI', 'Science Fiction'),
        ('BIO', 'Biography'),
        ('FAN', 'Fantasy'),
        ('MYST', 'Mystery'),
        ('ROM', 'Romance'),
        ('HIST', 'Historical'),
    ]

    title = models.CharField("Title", max_length=200)
    author = models.CharField("Author", max_length=200)
    genre = models.CharField(max_length=4, choices=GENRE_CHOICES, default='FIC')
    publication_year = models.PositiveIntegerField("Publication Year")

    class Meta:
        ordering = ['-publication_year']
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} by {self.author}"
