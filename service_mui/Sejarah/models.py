from django.db import models

class Sejarah(models.Model):
    isi_sejarah = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-id']
