# Generated by Django 2.2.3 on 2019-07-31 17:58

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
