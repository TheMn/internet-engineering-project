# Generated by Django 3.0 on 2019-12-15 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('postingApp', '0001_initial'), ('postingApp', '0002_auto_20191212_1139'), ('postingApp', '0003_auto_20191212_1211'), ('postingApp', '0004_auto_20191212_1213'), ('postingApp', '0005_comment'), ('postingApp', '0006_auto_20191212_1306'), ('postingApp', '0007_auto_20191212_1809'), ('postingApp', '0008_auto_20191212_1949'), ('postingApp', '0009_auto_20191212_1951'), ('postingApp', '0010_auto_20191214_1842'), ('postingApp', '0011_auto_20191214_1847'), ('postingApp', '0012_auto_20191214_1857'), ('postingApp', '0013_auto_20191214_1902'), ('postingApp', '0014_auto_20191214_1933'), ('postingApp', '0015_auto_20191214_1935'), ('postingApp', '0016_auto_20191215_1029'), ('postingApp', '0017_auto_20191215_1122')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='profile')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('date_joined', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(default='SOME STRING', max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Teacher'), (2, 'Student')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='postStuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postingApp.Profile')),
                ('text', models.TextField(max_length=400)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postingApp.PostStuff')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postingApp.Profile')),
                ('text', models.TextField()),
                ('cm_date', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postingApp.PostStuff')),
            ],
            options={
                'unique_together': {('post', 'author')},
            },
        ),
    ]