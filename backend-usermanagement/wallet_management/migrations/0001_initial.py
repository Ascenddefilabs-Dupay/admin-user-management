# Generated by Django 5.1.2 on 2024-10-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCurrency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wallet_id', models.CharField(max_length=255)),
                ('currency_type', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=8, default=0, max_digits=18)),
            ],
            options={
                'db_table': 'user_currencies',
                'managed': False,
            },
        ),
    ]