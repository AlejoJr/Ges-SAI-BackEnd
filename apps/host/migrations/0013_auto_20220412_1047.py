# Generated by Django 3.2.8 on 2022-04-12 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sai', '0009_rename_user_sai_userconnection'),
        ('host', '0012_auto_20220412_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostSai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host.host')),
                ('sai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sai.sai')),
                ('enchufado', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'HOST_SAI',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='sais',
            field=models.ManyToManyField(blank=True, related_name='sais_hosts', through='host.HostSai', to='sai.Sai'),
        ),
    ]
