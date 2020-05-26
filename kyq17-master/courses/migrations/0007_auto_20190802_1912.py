# Generated by Django 2.2.3 on 2019-08-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20190802_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='source',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source1',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source3',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source4',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source_title',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source_title1',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source_title2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source_title3',
        ),
        migrations.RemoveField(
            model_name='course',
            name='source_title4',
        ),
        migrations.AddField(
            model_name='language',
            name='source1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='source2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='source3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='source4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='source_title1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='source_title2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='source_title3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='language',
            name='source_title4',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]