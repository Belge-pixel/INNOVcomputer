from django.db import models

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    image = models.ImageField(upload_to='formations/', blank=True, null=True)

    def __str__(self):
        return self.titre
