# Generated by Django 3.2.3 on 2021-11-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_file',
            old_name='file',
            new_name='filename',
        ),
        migrations.AddField(
            model_name='upload_file',
            name='videoname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='videotype',
            field=models.CharField(default='', max_length=100),
        ),
    ]