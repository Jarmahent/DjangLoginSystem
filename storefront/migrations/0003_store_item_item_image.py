# Generated by Django 2.0.1 on 2018-07-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0002_auto_20180704_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='store_item',
            name='item_image',
            field=models.FileField(default='', upload_to='storefront/media/'),
        ),
    ]