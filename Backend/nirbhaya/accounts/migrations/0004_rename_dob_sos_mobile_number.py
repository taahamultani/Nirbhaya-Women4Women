# Generated by Django 4.1.2 on 2023-04-02 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_gender_sos_relation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sos',
            old_name='dob',
            new_name='mobile_number',
        ),
    ]
