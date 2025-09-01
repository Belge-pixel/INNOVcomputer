from django.db import models

# Create your models here.
class Formation(models.Model):
    titre_formation = models.CharField(max_length=50)
    description_formation = models.TextField()
    def __str__(self):
        return super().__str__()


class Cours(models.Model):
    nom_cours = models.CharField(max_length= 50)
    description_cours = models.CharField(max_length=100) 
    images_cours = models.ImageField(upload_to='cours_images/',default='')
    formation = models.ForeignKey(Formation,on_delete=models.CASCADE)
    
    def __str__(self):
        return super().__str__()


class Chapitre(models.Model):
    titre_chapitre = models.CharField(max_length=100)
    contenu_chapitre = models.TextField()   
    cours = models.ForeignKey(Cours,on_delete=models.CASCADE) 
    
    def __str__(self):
        return super().__str__()

class Expertise(models.Model):
    titre_expertise = models.CharField(max_length=50)
    contenu_expertise = models.TextField()    
    
    def __str__(self):
        return super().__str__()