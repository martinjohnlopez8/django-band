# Generated by Django 2.0.2 on 2018-02-14 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_released', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('image_link', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('year_formed', models.IntegerField()),
                ('place_of_origin', models.CharField(max_length=50)),
                ('image_link', models.CharField(blank=True, default='', max_length=255)),
                ('history', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=50)),
                ('image_link', models.CharField(blank=True, default='', max_length=255)),
                ('biography', models.TextField(blank=True, default='')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.Album')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.Band')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.Band'),
        ),
    ]