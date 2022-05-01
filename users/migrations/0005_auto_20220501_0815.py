# Generated by Django 3.2.5 on 2022-05-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_shop_store_pickle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pickles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_pickle', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='shop',
            name='store_pickle',
        ),
    ]
