# Generated by Django 2.1.10 on 2019-09-17 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='stories',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4+', '4+')], default='1', max_length=6, null=True),
        ),
    ]
