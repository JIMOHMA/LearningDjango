# Generated by Django 2.0.7 on 2021-01-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210114_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
