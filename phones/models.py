from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify


class Country(models.Model):
    """A model to represent countries."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class Brand(models.Model):
    """A model to represent cell phone brands."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name


class Feature(models.Model):

    class Color(models.TextChoices):
        WHITE = 'White'
        BLACK = 'Black'
        GOLD = 'Gold'
        SILVER = 'Silver'
        BLUE = 'Blue'
        YELLOW = 'Yellow'

    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='phones')
    color = models.CharField(
        max_length=50, choices=Color.choices, default=Color.WHITE)
    model = models.CharField(max_length=100, unique=True)
    made_in = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, related_name='phones_made_in')
    nationality = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, related_name='phones_origin')
    price = models.IntegerField(validators=[MinValueValidator(1)])
    screen_size = models.FloatField(validators=[MinValueValidator(1)])
    slug = models.SlugField(null=True)
    status = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=['brand']),
        ]
        ordering = ['brand']
        verbose_name = 'feature'
        verbose_name_plural = 'features'

    def brand_name(self):
        return self.brand.name

    def __str__(self):
        return f'{self.model}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.model)
        return super().save(*args, **kwargs)
