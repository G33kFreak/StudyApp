# Generated by Django 2.2 on 2020-06-29 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_auto_20200629_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classmodel',
            name='homework',
        ),
        migrations.AddField(
            model_name='homeworkmodel',
            name='Class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.ClassModel'),
        ),
    ]
