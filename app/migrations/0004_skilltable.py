# Generated by Django 5.1.4 on 2024-12-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_usertable_skill_delete_skilltable'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
