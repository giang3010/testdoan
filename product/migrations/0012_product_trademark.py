# Generated by Django 3.0.5 on 2020-06-07 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_trademark'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='trademark',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.TradeMark'),
            preserve_default=False,
        ),
    ]
