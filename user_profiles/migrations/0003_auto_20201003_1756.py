# Generated by Django 3.1.1 on 2020-10-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0002_auto_20201003_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
