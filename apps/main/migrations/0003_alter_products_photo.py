# Generated by Django 4.2.5 on 2023-09-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_products_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/photos', verbose_name='фото'),
        ),
    ]
