# Generated by Django 4.0.2 on 2022-05-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220501_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickles',
            old_name='store_pickle',
            new_name='store_pickle_after',
        ),
        migrations.AddField(
            model_name='pickles',
            name='store_pickle_before',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
