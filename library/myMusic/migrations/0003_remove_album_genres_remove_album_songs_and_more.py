# Generated by Django 4.2 on 2023-04-07 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myMusic', '0002_remove_song_genres_album_artists_album_artwork_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='albums',
        ),
        migrations.AddField(
            model_name='genre',
            name='albums',
            field=models.ManyToManyField(to='myMusic.album'),
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='artists',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='songs',
        ),
        migrations.AddField(
            model_name='playlist',
            name='albums',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myMusic.album'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='artists',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myMusic.artist'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myMusic.song'),
        ),
    ]
