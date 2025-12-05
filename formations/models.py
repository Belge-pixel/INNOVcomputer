from django.db import models

class Formation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    image = models.ImageField(upload_to='formations/', blank=True, null=True)
    points_cles = models.TextField(blank=True, null=True)  # champs pour les points clés

    def __str__(self):
        return self.titre

    def get_points_list(self):
        """Retourne la liste des points clés séparés par des virgules"""
        if self.points_cles:
            return [point.strip() for point in self.points_cles.split(",")]
        return []
