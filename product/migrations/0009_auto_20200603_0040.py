# Generated by Django 3.0.5 on 2020-06-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200601_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='variants',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=100),
        ),
    ]
