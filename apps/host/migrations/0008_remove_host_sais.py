# Generated by Django 3.2.8 on 2022-04-12 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0007_alter_host_sais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='sais',
        ),
    ]
