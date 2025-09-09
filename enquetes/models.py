from django.db import models
from django.utils import timezone
from django.conf import settings  

class Enquete(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    contenu = models.TextField()
    image = models.ImageField(upload_to='enquetes/', null=True, blank=True)
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    categorie = models.CharField(max_length=100, blank=True, null=True)
    a_la_une = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_publication']

    def __str__(self):
        return self.titre

    def get_excerpt(self, chars=200):
        return self.contenu[:chars] + '...' if len(self.contenu) > chars else self.contenu

class Commentaire(models.Model):
    enquete = models.ForeignKey(Enquete, related_name='commentaires', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    publie = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_creation']

    def __str__(self):
        return f"{self.nom} sur {self.enquete.titre}"
