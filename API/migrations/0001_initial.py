# Generated by Django 4.0.2 on 2022-03-31 06:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=255)),
                ('profile', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('content', tinymce.models.HTMLField()),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
    ]
