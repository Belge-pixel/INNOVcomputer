from django.shortcuts import render, redirect
from django.conf import settings
from .models import Contact
import urllib.parse
import requests

# Liste des numéros WhatsApp destinataires
WHATSAPP_NUMBERS = [
    "243810684080",  # Numéro principal
    # Ajouter d'autres numéros ici
]

def contact(request):
    success_message = ""
    error_message = ""

    if request.method == "POST":
        nom = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if nom and email and message:
            # Enregistrer le message dans la base
            contact_entry = Contact.objects.create(
                nom_customer_contact=nom,
                mail_customer_contact=email,
                message_customer_contact=message
            )

            # Préparer le message pour WhatsApp
            whatsapp_text = f"Nouveau message de contact\nNom: {nom}\nEmail: {email}\nMessage: {message}"
            whatsapp_text_encoded = urllib.parse.quote(whatsapp_text)

            # Créer les liens WhatsApp pour chaque numéro
            whatsapp_links = [f"https://api.callmebot.com/whatsapp.php?phone={number}&text={whatsapp_text_encoded}&apikey=5601173" for number in WHATSAPP_NUMBERS]

            # Envoyer le message via l'API CallMeBot
            for link in whatsapp_links:
                try:
                    response = requests.get(link)
                    if response.status_code == 200:
                        success_message = "Votre message a été envoyé et enregistré avec succès."
                    else:
                        error_message = "Erreur lors de l'envoi du message via WhatsApp."
                except Exception as e:
                    error_message = f"Erreur lors de l'envoi du message : {str(e)}"

            return render(request, "contact/contact.html", {
                "success_message": success_message,
                "error_message": error_message,
                "whatsapp_links": whatsapp_links
            })
        else:
            error_message = "Merci de remplir tous les champs du formulaire."

    return render(request, "contact/contact.html", {
        "error_message": error_message
    })
