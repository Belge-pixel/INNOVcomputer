from django.db import models

# Create your models here.
class Produit(models.Model):
    nom_produit = models.CharField(max_length=50)
    description_produit = models.TextField()
    version_produit = models.CharField(max_length=20)
    compatibilite_produit = models.CharField(max_length=20)
    licence_produit = models.CharField(max_length=50)
    categorie_produit = models.CharField(max_length = 50)
    image_produit = models.ImageField(upload_to="produits_images/" ,default='')
    
    def __str__(self):
        return super().__str__()


class DemandeDevis(models.Model):
        nom_customer_demane_devis = models.CharField(max_length=26)
        mail_customer_demande_devis =models.EmailField()
        message_demande_devis = models.TextField()
        produi_demande_devis = models.ForeignKey(Produit,on_delete=models.CASCADE)
        
        def __str__(self):
             return super().__str__()