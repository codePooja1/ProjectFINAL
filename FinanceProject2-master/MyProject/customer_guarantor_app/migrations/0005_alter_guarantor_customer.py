# Generated by Django 4.0.1 on 2022-01-18 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
        ('customer_guarantor_app', '0004_alter_guarantor_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guarantor',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Guarantor_set', to='Customer.customer'),
        ),
    ]
