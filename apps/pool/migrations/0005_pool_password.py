# Generated by Django 3.2.8 on 2022-03-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0004_pool_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]