# Generated by Django 4.2.5 on 2023-09-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_products_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Не указано', 'Без категории'), ('HM', 'Для дома'), ('CLTHS', 'Одежда'), ('SCHL', 'Школа'), ('DCH', 'Дача'), ('KDSFR', 'Для детей'), ('DCTN', 'Образование')], default='Не указано', max_length=10, verbose_name='категория'),
        ),
    ]
