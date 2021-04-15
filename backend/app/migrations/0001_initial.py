# Generated by Django 2.2 on 2020-12-01 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('is_limit_over', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'APIKey',
                'verbose_name_plural': 'APIKeys',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('publish_date_time', models.DateTimeField()),
                ('video_id', models.TextField()),
                ('channel_id', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='VideoThumbNail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_size', models.CharField(max_length=20)),
                ('url', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail', to='app.Video')),
            ],
            options={
                'verbose_name': 'Video ThumNail',
                'verbose_name_plural': 'Video ThumNails',
            },
        ),
    ]
