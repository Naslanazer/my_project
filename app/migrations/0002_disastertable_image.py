# Generated by Django 5.1.4 on 2024-12-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disastertable',
            name='Image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]