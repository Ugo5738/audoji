# Generated by Django 4.2.8 on 2024-02-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("audojifactory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiofile",
            name="cover_image",
            field=models.ImageField(blank=True, null=True, upload_to="cover_images/"),
        ),
    ]
