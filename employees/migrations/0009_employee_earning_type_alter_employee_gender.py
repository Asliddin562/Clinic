# Generated by Django 5.2.1 on 2025-06-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_profession_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='earning_type',
            field=models.CharField(choices=[('fixed', 'Fixed'), ('percentage', 'Percentage')], default='Fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', 'Man'), ('female', 'Woman')], default='Man', max_length=10),
        ),
    ]
