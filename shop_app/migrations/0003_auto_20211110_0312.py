

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_pin_tshirt'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
    ]
