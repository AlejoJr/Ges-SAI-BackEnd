# Generated by Django 3.2.8 on 2022-03-02 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0004_alter_host_sais'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='sais',
            new_name='sais_hosts',
        ),
    ]
