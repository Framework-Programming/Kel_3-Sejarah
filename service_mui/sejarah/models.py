from django.db import models


class Movie(models.Model):
    id_sejarah = models.IntegerField()
    isi_sejarah = models.CharField(max_length=100)
    # year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

