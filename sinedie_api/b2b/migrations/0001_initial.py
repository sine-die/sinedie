# Generated by Django 3.0.7 on 2020-06-30 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intermediate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=9)),
                ('max_capacity', models.IntegerField()),
                ('cur_capacity', models.IntegerField()),
                ('business_type', models.CharField(choices=[(0, 'bar'), (1, 'restaurant'), (2, 'shop'), (3, 'gym'), (4, 'other')], max_length=200)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'business_users',
            },
        ),
    ]
