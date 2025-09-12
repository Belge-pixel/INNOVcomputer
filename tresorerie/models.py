from django.db import models

# Create your models here.
class Caisee(models.Model):
    solde_actuel = models.FloatField()
    total_depense_caisse = models.FloatField()
    nombre_transactions_caisse = models.IntegerField()
    
class Transaction(models.Model):
    date_transaction = models.DateTimeField(auto_now_add=False)    
    categorie_transaction = models.CharField(max_length=20)
    type_transaction = models.CharField(max_length=10)
    montant_transaction = models.FloatField()
    note_transaction = models.CharField(max_length=20)
    # caisse = models.ForeignKey(Caisee,on_delete=models.CASCADE)
    
    def __str__(self):
        return super().__str__()