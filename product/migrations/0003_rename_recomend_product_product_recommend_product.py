# Generated by Django 4.1.3 on 2023-01-06 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_recomend_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='recomend_product',
            new_name='recommend_product',
        ),
    ]
