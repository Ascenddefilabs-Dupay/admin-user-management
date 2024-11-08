# Generated by Django 5.1.2 on 2024-10-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('user_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_first_name', models.CharField(max_length=30)),
                ('user_middle_name', models.CharField(blank=True, max_length=30)),
                ('user_last_name', models.CharField(max_length=30)),
                ('user_dob', models.DateField()),
                ('user_phone_number', models.BigIntegerField()),
                ('user_password', models.CharField()),
                ('user_status', models.BooleanField(default=False)),
                ('user_hold', models.BooleanField(default=False)),
                ('user_type', models.CharField()),
                ('profile_privacy', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=10)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
