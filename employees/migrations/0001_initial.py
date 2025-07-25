# Generated by Django 5.2.1 on 2025-05-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('father_name', models.CharField(blank=True, max_length=30, null=True)),
                ('mobile_phone', models.CharField(max_length=20)),
                ('home_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(choices=[('male', 'Man'), ('female', 'Woman')], max_length=10)),
                ('profession', models.CharField(blank=True, choices=[('director', 'Director'), ('admin', 'Administrator'), ('manager', 'Manager'), ('accountant', 'Accountant'), ('receptionist', 'Receptionist'), ('doctor', 'Doctor'), ('dentist', 'Dentist'), ('pediatrician', 'Pediatrician'), ('cardiologist', 'Cardiologist'), ('neurologist', 'Neurologist'), ('surgeon', 'Surgeon'), ('gynecologist', 'Gynecologist'), ('dermatologist', 'Dermatologist'), ('psychiatrist', 'Psychiatrist'), ('therapist', 'Therapist'), ('nurse', 'Nurse'), ('pharmacist', 'Pharmacist'), ('assistant', 'Assistant'), ('guard', 'Guard')], max_length=50, null=True)),
                ('is_accepting_appointments', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=30)),
                ('home', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
            ],
        ),
    ]
