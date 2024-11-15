# Generated by Django 3.2.14 on 2023-06-07 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='etpflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dnt', models.DateTimeField(auto_now_add=True)),
                ('smno', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('fstatus', models.CharField(max_length=25)),
                ('ib', models.CharField(max_length=25)),
                ('ob', models.CharField(max_length=25)),
                ('etp', models.CharField(max_length=25)),
                ('obh', models.CharField(max_length=25)),
                ('flowvalue', models.DecimalField(decimal_places=2, max_digits=15)),
                ('tot', models.DecimalField(decimal_places=2, max_digits=15)),
                ('itp1', models.CharField(max_length=25)),
                ('itp2', models.CharField(max_length=25)),
                ('ffp1', models.CharField(max_length=25)),
                ('ffp2', models.CharField(max_length=25)),
                ('b1', models.CharField(max_length=25)),
                ('b2', models.CharField(max_length=25)),
                ('stp1', models.CharField(max_length=25)),
                ('stp2', models.CharField(max_length=25)),
                ('pos', models.CharField(max_length=25)),
                ('nop', models.CharField(max_length=25)),
                ('itpr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ffpr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('blwrr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stpr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('itpc', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ffpc', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bwlrc', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stpc', models.DecimalField(decimal_places=2, max_digits=15)),
                ('mpv', models.DecimalField(decimal_places=2, max_digits=15)),
                ('nobkwsh', models.DecimalField(decimal_places=2, max_digits=15)),
                ('itpophr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('ffpophr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('blwrophr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stpophr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stpserhr', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stpon', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('smno', models.CharField(max_length=25)),
                ('lat', models.CharField(max_length=25)),
                ('lon', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25)),
                ('quota', models.IntegerField()),
                ('techno', models.CharField(max_length=150)),
                ('techemail', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('dnt', models.DateTimeField(auto_now_add=True)),
                ('rd', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=15)),
                ('mobileno', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=40)),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zname', models.CharField(max_length=55)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etp.site')),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('uemail', models.CharField(max_length=120)),
                ('umob', models.CharField(max_length=20)),
                ('mdate', models.DateTimeField()),
                ('Desc', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=10)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etp.site')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='fault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('dnt', models.DateTimeField(auto_now_add=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etp.site')),
            ],
        ),
        migrations.CreateModel(
            name='User_addon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.CharField(max_length=15)),
                ('company_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('password_text', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'company_name')},
            },
        ),
    ]
