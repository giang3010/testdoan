# Generated by Django 2.2.7 on 2020-05-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200522_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/images/8ts20a001-so001-m_6A2DGHn.jpg', null=True, upload_to='images/'),
        ),
    ]
