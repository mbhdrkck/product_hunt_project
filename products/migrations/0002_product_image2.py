# Generated by Django 2.1.5 on 2019-04-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
