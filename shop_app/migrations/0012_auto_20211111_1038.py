# Generated by Django 3.2.9 on 2021-11-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0011_productfeatures_productfeaturevalidators'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfeaturevalidators',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productfeaturevalidators',
            name='feature',
        ),
        migrations.DeleteModel(
            name='ProductFeatures',
        ),
        migrations.DeleteModel(
            name='ProductFeatureValidators',
        ),
    ]
