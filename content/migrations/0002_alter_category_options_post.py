# Generated by Django 5.0 on 2025-02-05 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('featured_image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('short_description', models.TextField(max_length=500)),
                ('blog_body', models.TextField(max_length=5000)),
                ('is_featured', models.BooleanField(default=False)),
                ('status', models.BooleanField(choices=[(True, 'Published'), (False, 'Draft')], default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.category')),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
