# Generated by Django 5.0.1 on 2024-02-04 15:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('text', models.TextField(max_length=10000, verbose_name='Text')),
                ('delete_option', models.CharField(choices=[('SPECIFIC_DATE', 'Delete on specific date and time'), ('AFTER_READ', 'Delete after read'), ('NEVER', 'Never delete')], default='NEVER', max_length=20, verbose_name='Delete Option')),
                ('delete_at', models.DateTimeField(blank=True, null=True, verbose_name='Delete At')),
                ('is_deactivated', models.BooleanField(default=False, verbose_name='Deactivated')),
                ('status', models.CharField(choices=[('public', 'Public'), ('unlisted', 'Unlisted'), ('private', 'Private')], default='public', max_length=20, verbose_name='Paste Status')),
                ('slug', models.SlugField(blank=True, max_length=10, verbose_name='Slug')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time')),
                ('views', models.PositiveIntegerField(default=0, null=True, verbose_name='Views')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pastes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Paste',
                'verbose_name_plural': 'Pastes',
                'db_table': 'paste',
                'ordering': ['-date'],
            },
        ),
    ]