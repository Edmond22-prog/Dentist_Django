from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html", {})


def contact(request):
    #Verifie s'il s'agit d'un POST ou d'un clique sur le lien
    if (request.method == "POST"):
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # Envoi d'un email
        send_mail (
            message_name, # Sujet
            message, # Message
            message_email, # Email de l'envoyeur
            ['edghimakoll@gmail.com'], # Email du receveur
        )
        return render(request, "contact.html", {'message_name': message_name})
    else:
        return render(request, "contact.html", {})


def about(request):
    return render(request, "about.html", {})


def pricing(request):
    return render(request, "pricing.html", {})


def service(request):
    return render(request, "service.html", {})