# Generated by Django 4.1.7 on 2024-11-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('в наличии', 'в наличии'), ('выдана', 'выдана')], max_length=255)),
            ],
        ),
    ]
