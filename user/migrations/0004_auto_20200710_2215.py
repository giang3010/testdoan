# Generated by Django 3.0.5 on 2020-07-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_listaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaddress',
            name='city',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listaddress',
            name='country',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
