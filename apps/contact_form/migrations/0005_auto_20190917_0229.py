# Generated by Django 2.1.10 on 2019-09-17 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0004_contactform_service_house_wash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='stories',
            new_name='number_of_stories',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='service_house_wash',
            new_name='soft_wash',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='exterior',
            new_name='type_of_exterior',
        ),
        migrations.AddField(
            model_name='contactform',
            name='deck_cleaning',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='contactform',
            name='fence_cleaning',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='contactform',
            name='outdoor_stain_removal',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='contactform',
            name='surface_cleaning',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
