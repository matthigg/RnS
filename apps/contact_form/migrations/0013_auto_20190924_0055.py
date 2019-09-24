# Generated by Django 2.1.10 on 2019-09-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0012_auto_20190924_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='number_of_stories',
            field=models.CharField(choices=[('Not_Specified', 'Select'), ('1', '1'), ('2', '2'), ('3', '3'), ('4+', '4+')], default='Not_Specified', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='type_of_exterior',
            field=models.CharField(choices=[('Not_Specified', 'Select'), ('Vinyl', 'Vinyl'), ('Wood', 'Wood'), ('Brick', 'Brick'), ('Aluminum', 'Aluminum'), ('Other', 'Other')], default='Not_Specified', max_length=24, null=True),
        ),
    ]
