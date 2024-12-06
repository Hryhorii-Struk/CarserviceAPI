# Generated by Django 4.2.1 on 2023-06-09 12:58

import apps.service_app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web_app', '0001_initial'),
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField()),
                ('image', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField()),
                ('year', models.DateField()),
                ('VIN', models.CharField()),
                ('repair', models.BooleanField(default=False)),
                ('kilometers', models.CharField(blank=True, null=True)),
                ('registration_number', models.CharField(blank=True, null=True, unique=True)),
                ('have_history', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service_app.carbrand')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.customerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('position', models.CharField(blank=True, choices=[('Mechanic', 'Mechanic'), ('Reciver', 'Reciver')], max_length=10, null=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RepairHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.JSONField(default=apps.service_app.models.RepairHistory.default_json)),
                ('car_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='service_app.cars')),
            ],
        ),
        migrations.CreateModel(
            name='CarQueue',
            fields=[
                ('car_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='service_app.cars')),
                ('status', models.CharField(blank=True, choices=[('Awaiting To Take', 'Awaiting To Take'), ('Investigating Car', 'Investigating Car'), ('In Progress', 'In Progress'), ('Done', 'Done')], max_length=20, null=True)),
                ('mechanic_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service_app.personalprofile')),
            ],
        ),
    ]
