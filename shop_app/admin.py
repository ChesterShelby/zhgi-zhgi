from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe       # Нужно для ограничения разрешения изображения
from PIL import Image                               # Нужно для ограничения разрешения изображения

from .models import *

# Нужно для ограничения разрешения изображения
"""class AdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = \
            mark_safe('<span style="color:red; font-size:14px;">Загружайте изображения с минимальным разрешением {}x{}'
                      ' и максимальным {}x{}</span>'.format(*Product.MIN_RESOLUTION,  *Product.MAX_RESOLUTION))
        
    def clean_image(self):
        
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_widht, min_height = Product.MIN_RESOLUTION
        max_widht, max_height = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер загружаемого изображения больше допустимого (10МБ)')
        if img.widht < min_widht or img.height < min_height:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.widht > max_widht or img.height > max_height:
            raise ValidationError('Разрешение изображения больше максимального!')
        return image"""


class TshirtAdmin(admin.ModelAdmin):

    # form = AdminForm       # Нужно для ограничения разрешения изображения

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='t-shirt'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PinsAdmin(admin.ModelAdmin):

    # form = AdminForm       # Нужно для ограничения разрешения изображения

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='pins'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Tshirt, TshirtAdmin)
admin.site.register(Pin, PinsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)

