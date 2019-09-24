# Generated by Django 2.1.10 on 2019-09-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0006_auto_20190924_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='number_of_stories',
            field=models.CharField(choices=[('Not specified', 'Select'), ('1', '1'), ('2', '2'), ('3', '3'), ('4+', '4+')], default='Not specified', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='type_of_exterior',
            field=models.CharField(blank=True, choices=[('Not specified', 'Select'), ('Vinyl', 'Vinyl'), ('Wood', 'Wood'), ('Brick', 'Brick'), ('Aluminum', 'Aluminum'), ('Other', 'Other')], default='Not specified', max_length=24, null=True),
        ),
    ]
