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


class Mission(models.Model):
    """Modèle pour stocker les missions/valeurs de l'entreprise"""
    titre_mission = models.CharField(max_length=100)
    description_mission = models.TextField()
    icone_fa = models.CharField(max_length=50, default='fas fa-star', help_text="Classe Font Awesome (ex: fas fa-graduation-cap)")
    couleur_theme = models.CharField(max_length=20, default='blue', 
                                     choices=[
                                         ('blue', 'Bleu'),
                                         ('green', 'Vert'),
                                         ('purple', 'Violet'),
                                         ('red', 'Rouge'),
                                         ('yellow', 'Jaune'),
                                         ('pink', 'Rose'),
                                     ],
                                     help_text="Couleur de la carte")
    ordre = models.IntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['ordre']
        verbose_name = 'Mission'
        verbose_name_plural = 'Missions'
    
    def __str__(self):
        return self.titre_mission
        return self.titre_mission


class Responsable(models.Model):
    """Modèle pour stocker les responsables/équipe de l'entreprise"""
    nom_responsable = models.CharField(max_length=100)
    prenom_responsable = models.CharField(max_length=100)
    photo_responsable = models.ImageField(upload_to='responsables/', null=True, blank=True)
    role_principal = models.CharField(max_length=100, help_text="Ex: Directeur Technique")
    specialite = models.CharField(max_length=100, help_text="Ex: Expert en Développement")
    description = models.TextField()
    ordre = models.IntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['ordre']
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'
    
    def __str__(self):
        return f"{self.prenom_responsable} {self.nom_responsable}"
    
    @property
    def nom_complet(self):
        return f"{self.prenom_responsable} {self.nom_responsable}"