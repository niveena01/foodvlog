from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class catego(models.Model):
    objects = None
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_url(self):
        return reverse('prod_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class products(models.Model):
    objects = None
    name = models.CharField(max_length=123, unique=True)
    slug = models.CharField(max_length=123, unique=True)
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(catego, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Item:
    pass
