# Generated by Django 3.0.4 on 2022-06-11 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myappblogpost',
            options={'ordering': ['-timestamp']},
        ),
    ]