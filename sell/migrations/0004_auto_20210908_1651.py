# Generated by Django 3.0.7 on 2021-09-08 16:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_product_cost_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sell', '0003_auto_20210906_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(blank=True, max_length=50)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_sold', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Product')),
                ('sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sell.Sell')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.DeleteModel(
            name='SellProduct',
        ),
        migrations.AddField(
            model_name='sell',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sell.Customer'),
        ),
    ]
