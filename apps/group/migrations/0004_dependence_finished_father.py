# Generated by Django 3.2.8 on 2022-04-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_dependence'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependence',
            name='finished_father',
            field=models.BooleanField(null=True),
        ),
    ]