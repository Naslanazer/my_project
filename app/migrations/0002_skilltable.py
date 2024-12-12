# Generated by Django 5.1.4 on 2024-12-12 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill', models.CharField(blank=True, max_length=30, null=True)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usertable')),
            ],
        ),
    ]
