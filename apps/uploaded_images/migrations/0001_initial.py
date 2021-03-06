# Generated by Django 2.1.10 on 2019-09-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(choices=[('No_Category', 'Select a Category'), ('Concrete_and_Brick', 'Concrete & Brick'), ('Decks', 'Decks'), ('Deck_Staining', 'Deck Staining'), ('Driveways', 'Driveways'), ('Fences', 'Fences'), ('Graffiti_Removal', 'Graffiti Removal'), ('Houses', 'Houses'), ('Sidewalks', 'Sidewalks')], default='None', max_length=64, null=True)),
                ('Before_Picture_Description', models.CharField(blank=True, max_length=64, null=True)),
                ('Before_Picture_Size_kB', models.IntegerField(default=140, null=True)),
                ('Before_Picture_Max_Dimension', models.IntegerField(default=768, null=True)),
                ('Before_Picture', models.ImageField(null=True, upload_to='images/')),
                ('After_Picture_Description', models.CharField(blank=True, max_length=64, null=True)),
                ('After_Picture_Size_kB', models.IntegerField(default=140, null=True)),
                ('After_Picture_Max_Dimension', models.IntegerField(default=768, null=True)),
                ('After_Picture', models.ImageField(null=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Notes', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Uploaded Images',
            },
        ),
    ]
