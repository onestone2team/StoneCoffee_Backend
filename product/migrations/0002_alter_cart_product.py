# Generated by Django 4.1.3 on 2022-12-06 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
