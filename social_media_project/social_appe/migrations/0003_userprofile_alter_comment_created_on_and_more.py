# Generated by Django 4.1.3 on 2022-12-02 10:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social_appe', '0002_alter_post_created_on_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(default='uploads/profile_pictures/default.png', upload_to='upload/profile_pictures')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 10, 47, 56, 226418, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 10, 47, 56, 225421, tzinfo=datetime.timezone.utc)),
        ),
    ]
