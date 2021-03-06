# Generated by Django 2.1.10 on 2019-09-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploaded_single_images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedSingleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(choices=[('No_Category', 'Select a Category'), ('House_Wash', 'House Wash'), ('Wood_Restoring', 'Wood Restoring'), ('Oxidation_Removal', 'Oxidation Removal'), ('Stain_Removal', 'Stain Removal')], default='No_Category', max_length=64, null=True)),
                ('Single_Picture_Description', models.CharField(blank=True, max_length=64, null=True)),
                ('Single_Picture_Size_kB', models.IntegerField(default=140, null=True)),
                ('Single_Picture_Max_Dimension', models.IntegerField(default=768, null=True)),
                ('Single_Picture_Rotation', models.IntegerField(choices=[(0, '0 degrees'), (270, '90 degrees (90 degrees clockwise)'), (180, '180 degrees (upside-down)'), (90, '270 degrees (90 degrees counter-clockwise)')], default=0, null=True)),
                ('Single_Picture', models.ImageField(null=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Notes', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Uploaded Single Images',
            },
        ),
        migrations.DeleteModel(
            name='UploadedImages',
        ),
    ]
