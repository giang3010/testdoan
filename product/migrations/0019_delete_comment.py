# Generated by Django 3.0.5 on 2020-07-10 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
