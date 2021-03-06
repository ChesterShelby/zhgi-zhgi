

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('descriptions', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('descriptions', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
                ('thematics', models.CharField(max_length=255, verbose_name='Тематика')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
