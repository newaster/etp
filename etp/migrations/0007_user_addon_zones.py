# Generated by Django 3.2.14 on 2023-06-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etp', '0006_auto_20230608_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_addon',
            name='zones',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
