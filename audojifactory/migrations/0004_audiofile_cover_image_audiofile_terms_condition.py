# Generated by Django 4.2.8 on 2024-01-24 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audojifactory", "0003_audiosegment_mood"),
    ]

    operations = [
        migrations.AddField(
            model_name="audiofile",
            name="cover_image",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="audiofile",
            name="terms_condition",
            field=models.BooleanField(default=False),
        ),
    ]