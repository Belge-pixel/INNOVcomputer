from django.db import models

# Create your models here.
class Contact(models.Model):
    nom_customer_contact = models.CharField(max_length=26)
    mail_customer_contact = models.EmailField()
    message_customer_contact = models.TextField()
    
    def __str__(self):
        return super().__str__()