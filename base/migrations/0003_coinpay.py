# Generated by Django 4.1.3 on 2022-11-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_giftcard_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('amount', models.CharField(max_length=50)),
                ('is_anonymous', models.BooleanField()),
                ('is_paid', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
