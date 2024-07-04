from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-name',)

    def __str__(self):
        return self.name

    # Setting absolute URL
    def get_absolute_url(self):
        return reverse('main:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=180, null=True)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images')
    price = models.IntegerField()
    rating = models.FloatField(default=3)

    class Meta:
        ordering = ('time',)

class Portfolio_listings(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    client = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_gallery')
    description = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
