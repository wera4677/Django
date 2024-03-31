from django.db import models
# Create your models here.

class Album(models.Model):
    album_id = models.AutoField(primary_key=True, db_column='AlbumId')
    title = models.TextField(db_column='Title')
    artist = models.ForeignKey('Artist', on_delete=models.DO_NOTHING, db_column='ArtistId')

    class Meta:
        managed = False
        db_table = 'albums'

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True, db_column='ArtistId')
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'
