# Generated by Django 3.0.5 on 2020-07-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200728_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Nữ', 'Nữ'), ('Nam', 'Nam'), ('Chưa xác định', 'Chưa xác định')], default='Chưa xác định', max_length=20, null=True),
        ),
    ]
