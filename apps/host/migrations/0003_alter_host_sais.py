# Generated by Django 3.2.8 on 2022-03-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sai', '0009_rename_user_sai_userconnection'),
        ('host', '0002_host_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='sais',
            field=models.ManyToManyField(null=True, related_name='sais_hosts', to='sai.Sai'),
        ),
    ]