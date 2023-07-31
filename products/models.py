from django.db import models
import random

M_OR_F = (
    (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Unisex'),
    )
)


class Common(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Brand(Common):

    class Meta:
        verbose_name_plural = 'Brands'

    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
    )


class Domain(Common):

    class Meta:
        verbose_name_plural = 'Domains'

    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
    )


class Category(Common):

    class Meta:
        verbose_name_plural = 'Categories'

    friendly_name = models.CharField(
        max_length=254, null=True, blank=True
    )
    domain = models.ForeignKey(
        'Domain', null=True, blank=True,
        on_delete=models.SET_NULL
    )

    def get_friendly_name(self):
        return self.friendly_name


class Product(Common):

    class Meta:
        verbose_name_plural = 'Products'

    brand = models.ForeignKey(
        'Brand', null=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        'Category', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    domain = models.IntegerField(blank=True)
    sku = models.CharField(
        max_length=254, null=True, blank=True
    )
    description = models.TextField()
    has_sizes = models.BooleanField(
        default=False, null=True, blank=True,
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2
    )
    rating = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=True, blank=True
    )
    image_url = models.URLField(
        max_length=1024, null=True, blank=True
    )
    image = models.ImageField(
        null=True, blank=True
    )
    m_or_f = models.CharField(
        null=True, max_length=254, choices=M_OR_F
    )

    def save(self, *args, **kwargs):
        '''
        Autofills domain and sku
        '''
        if not self.domain:
            self.domain = self.category.domain.id

        if not self.sku:
            self.sku = (
                f'{self.category.domain.id}' +
                f'{self.brand.id}' +
                f'{self.category.id}' +
                str(random.randint(10000, 99999))
            )

        super().save(*args, **kwargs)
