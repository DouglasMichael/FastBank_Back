# Generated by Django 4.2 on 2023-05-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_FastBank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
