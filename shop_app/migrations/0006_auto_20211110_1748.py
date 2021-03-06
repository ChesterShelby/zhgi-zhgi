

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_alter_cart_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=28, null=True, verbose_name='Номер телефона'),
        ),
    ]
