from django.db import models


class Sejarah(models.Model):
    id_sejarah = models.IntegerField(max_length=11)
    isi_sejarah = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-id']


