# Generated by Django 3.2.14 on 2023-06-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etp', '0003_alter_user_addon_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='zones',
            name='assignedto',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
