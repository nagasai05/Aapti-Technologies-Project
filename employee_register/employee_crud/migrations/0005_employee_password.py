# Generated by Django 4.0.4 on 2022-05-17 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_crud', '0004_employee_role_alter_employee_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='********', max_length=50),
        ),
    ]
