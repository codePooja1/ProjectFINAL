# Generated by Django 4.0.1 on 2022-01-18 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
        ('AddressApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permanentaddress',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paddress', to='Customer.customer'),
        ),
    ]
