# Generated by Django 5.0.7 on 2024-07-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LightSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=7)),
                ('intensity', models.IntegerField()),
                ('pattern', models.CharField(max_length=20)),
            ],
        ),
    ]
