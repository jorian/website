from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(verbose_name='e-mail')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
