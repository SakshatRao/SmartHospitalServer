# Generated by Django 3.1.3 on 2020-11-05 07:43

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
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_email', models.EmailField(default='', max_length=254, unique=True)),
                ('DOB', models.DateField(verbose_name='Birth Date')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=50)),
                ('contact', models.CharField(default='', max_length=10)),
                ('street_address', models.TextField(default='', max_length=200)),
                ('pin_code', models.CharField(default='', max_length=6)),
                ('occupation', models.CharField(choices=[('D', 'Doctor'), ('N', 'Nurse')], default='D', max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_email', models.EmailField(default='', max_length=254, unique=True)),
                ('DOB', models.DateField(verbose_name='Birth Date')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=50)),
                ('contact', models.CharField(default='', max_length=10)),
                ('street_address', models.TextField(default='', max_length=200)),
                ('pin_code', models.CharField(default='', max_length=6)),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='A+', max_length=5)),
                ('room_number', models.IntegerField(blank=True, null=True, unique=True)),
                ('is_validated', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='All_Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(default='', max_length=50)),
                ('staff_email', models.EmailField(default='', max_length=254, unique=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('staff', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.staff')),
            ],
        ),
        migrations.CreateModel(
            name='All_Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(default='', max_length=50)),
                ('patient_email', models.EmailField(default='', max_length=254, unique=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('discharge_date', models.DateField(blank=True, null=True)),
                ('patient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.patient')),
            ],
        ),
    ]
