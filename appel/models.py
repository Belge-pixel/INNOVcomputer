from django.db import models

class Appel(models.Model):
    nom_appelant = models.CharField(max_length=100)
    numero_appelant = models.CharField(max_length=20)
    numero_destinataire = models.CharField(max_length=20)
    date_appel = models.DateTimeField(auto_now_add=True)
    duree_appel = models.DurationField(null=True, blank=True)
    statut_appel = models.CharField(max_length=20, choices=[
        ('entrant', 'Appel entrant'),
        ('sortant', 'Appel sortant'),
        ('manque', 'Appel manqué'),
        ('termine', 'Appel terminé'),
    ], default='entrant')
    type_appel = models.CharField(max_length=10, choices=[
        ('audio', 'Audio'),
        ('video', 'Vidéo'),
    ], default='audio')

    def __str__(self):
        return f"Appel de {self.nom_appelant} - {self.statut_appel}"
