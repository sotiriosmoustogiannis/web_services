# Generated by Django 3.2.5 on 2022-04-30 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_shop_store_pickle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='store_pickle',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
