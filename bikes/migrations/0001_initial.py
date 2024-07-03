# Generated by Django 4.1.3 on 2022-12-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('contact_number', models.CharField(max_length=13)),
                ('vehicle_type', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=20)),
                ('model_name', models.CharField(max_length=20)),
                ('year_of_purchase', models.DateField()),
                ('kilometers', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('registered_state', models.CharField(max_length=20)),
                ('num_of_oweners', models.IntegerField()),
                ('payment_mode', models.CharField(max_length=20)),
            ],
        ),
    ]