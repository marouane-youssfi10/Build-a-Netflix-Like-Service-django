# Generated by Django 3.1.3 on 2022-03-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0006_tvshowproxy_tvshowseasonproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='type',
            field=models.CharField(choices=[('MOV', 'Movie'), ('TVS', 'TV Show'), ('SEA', 'Season'), ('PLY', 'Playlist')], default='PLY', max_length=3),
        ),
    ]
