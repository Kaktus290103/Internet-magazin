from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category',
                        args=[self.slug])

class Tovary(models.Model):
    name = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    colsklad = models.IntegerField(null=True)
    sale = models.IntegerField(blank=True) 
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=None)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail',
                        args=[self.id, self.slug])    

    

