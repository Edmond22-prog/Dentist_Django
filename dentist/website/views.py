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


def appointment(request):
    #Verifie s'il s'agit d'un POST ou d'un clique sur le lien
    if (request.method == "POST"):
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        appointment = "Name: "+ your_name + " Phone: "+ your_phone +" Email: "+ your_email +" Address: "+ your_address +" Schedule: "+ your_schedule +" Day: "+ your_date +" Message: "+ your_message
        # Envoi d'un email
        send_mail (
            'Appointment Request', # Sujet
            appointment, # Message
            your_email, # Email de l'envoyeur
            ['edghimakoll@gmail.com'], # Email du receveur
        )
        return render(request, "appointment.html", {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_date': your_date,
            'your_message': your_message
            })
    else:
        return render(request, "home.html", {})