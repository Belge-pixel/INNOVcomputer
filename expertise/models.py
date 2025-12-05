from django.db import models

class Expertise(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    icone = models.CharField(max_length=100, help_text="Nom de l’icône (par ex. 'fa-solid fa-code')")
    image = models.ImageField(upload_to='expertise_images/', blank=True, null=True)

    def __str__(self):
        return self.titre
