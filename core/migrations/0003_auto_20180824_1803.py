# Generated by Django 2.0.2 on 2018-08-24 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180824_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name')},
        ),
    ]
