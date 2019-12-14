# Generated by Django 3.0 on 2019-12-14 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postingApp', '0010_auto_20191214_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postingApp.PostStuff'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postingApp.PostStuff'),
        ),
    ]
