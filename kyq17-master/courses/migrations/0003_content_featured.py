# Generated by Django 2.2.3 on 2019-08-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_content_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='featured',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]