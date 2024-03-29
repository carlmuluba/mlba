# Generated by Django 4.0.4 on 2022-06-11 14:39

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mlba_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrbanImgMultiple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urban_tb', models.CharField(max_length=200)),
                ('cl_img_multiple', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('urban_image_tb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urban_img_tb', to='mlba_site.urbanimage')),
            ],
            options={
                'db_table': 'urban_img_multiple',
            },
        ),
    ]
