# Generated by Django 5.0.6 on 2024-05-11 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=200)),
                ('pr_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('pr_Description', models.TextField()),
                ('pr_image', models.ImageField(upload_to='media')),
                ('Priority', models.IntegerField(default=0)),
                ('delete_status', models.IntegerField(choices=[(1, 'live'), (0, 'delete')], default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('Brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='Products.brands')),
            ],
        ),
    ]
