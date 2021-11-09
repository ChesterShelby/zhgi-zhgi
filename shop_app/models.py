from PIL import Image      # Нужно для ограничения разрешения изображения

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


User = get_user_model()


def get_product_url(obj, view_name):
    ct_model = obj.__class__._meta.model_name
    return reverse(view_name, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    objects = LatestProductsManager()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


# Нужно для ограничения разрешения изображения
"""class MinResolutionErrorException(Exception):
    pass


class MaxResolutionErrorException(Exception):
    pass"""


class Product(models.Model):

    MIN_RESOLUTION = (400, 400)
    MAX_RESOLUTION = (4000, 4000)
    MAX_IMAGE_SIZE = 10485760

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    descriptions = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    # Нужно для ограничения разрешения изображения
    """
    def save(self, *args, **kwargs):

        image = self.image
        img = Image.open(image)
        min_widht, min_height = self.MIN_RESOLUTION
        max_widht, max_height = self.MAX_RESOLUTION
        if img.widht < min_widht or img.height < min_height:
            raise MinResolutionErrorException('Разрешение изображения меньше минимального!')
        if img.widht > max_widht or img.height > max_height:
            raise MaxResolutionErrorException('Разрешение изображения больше максимального!')
        super().save(*args, **kwargs)"""


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {}(для корзины)".format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    product = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=28, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Tshirt(Product):

    size = models.CharField(max_length=255, verbose_name='Размер')
    color = models.CharField(max_length=255, verbose_name='Цвет')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')


class Pin(Product):

    size = models.CharField(max_length=255, verbose_name='Размер')
    thematics = models.CharField(max_length=255, verbose_name='Тематика')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolut_url(self):
        return get_product_url(self, 'product_detail')
