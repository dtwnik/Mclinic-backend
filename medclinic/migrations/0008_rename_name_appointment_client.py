# Generated by Django 4.0.5 on 2022-06-11 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medclinic', '0007_alter_appointment_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='client',
        ),
    ]