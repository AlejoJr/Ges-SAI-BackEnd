# Generated by Django 3.2.8 on 2022-03-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sai', '0009_rename_user_sai_userconnection'),
        ('host', '0003_alter_host_sais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='sais',
            field=models.ManyToManyField(related_name='sais_hosts', to='sai.Sai'),
        ),
    ]
