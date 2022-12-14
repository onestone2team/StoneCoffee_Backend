# Generated by Django 4.1.3 on 2022-12-26 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=50)),
                ('order_price', models.IntegerField(blank=True)),
                ('count', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('user_address', models.TextField()),
                ('user_phone', models.CharField(max_length=15)),
                ('weight', models.IntegerField(verbose_name='상품 중량')),
                ('product_image', models.ImageField(upload_to='%y/%m/')),
                ('receiver', models.TextField()),
                ('order_code', models.TextField(unique=True)),
                ('status', models.IntegerField(default=0, verbose_name='주문 상태')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('total_price', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderCancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_product', to='order.order')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_num', to='order.payment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='username', to='order.payment')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
