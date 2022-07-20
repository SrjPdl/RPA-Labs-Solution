# Generated by Django 4.0.6 on 2022-07-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0002_rename_created_at_video_upload_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='length',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='video',
            name='size',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload_timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
