# Generated by Django 4.0.6 on 2022-07-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testtask', '0003_auto_20220713_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
