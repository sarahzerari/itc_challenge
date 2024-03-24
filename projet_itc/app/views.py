from django.shortcuts import render
    
def home(request):
     return render(request,'index.html')
 
def succes(request):
     return render(request,'succes.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        family_name = request.POST.get('family')
        email = request.POST.get('email')
        number_of_persons = request.POST.get('nbr_personne', 0)
        date = request.POST.get('date')
        duration_type = request.POST.get('hmy')
        time = request.POST.get('time')
        duration = request.POST.get('hours', 0)

        # Validate your inputs as needed here
        if not name or not email:  # Simplistic validation example
            return HttpResponse("Invalid input.", status=400)

        # Save the data to your model
        registration = Registration(
            name=name,
            family_name=family_name,
            email=email,
            number_of_persons=number_of_persons,
            date=date,
            duration_type=duration_type,
            time=time,
            duration=duration
        )
        registration.save()
        send_email(email=email,message="your demmande is on treatment ")
        
        # Redirect or return a success response
        return redirect("succes") # Replace 'success_url' with your actual URL name
    else:
        return render(request, 'index.html')
    
import smtplib
import json
from email.message import EmailMessage
def send_email(email:str,message:str):
 #load config (gmail) from json file
     gmail_cfg = {
        "server": "smtp.gmail.com",
        "port": "465",
        "email": "TEST.1234.TEST.PYTHON@gmail.com",
        "pwd": "iszdppmfawgkgren"
     }
     msg=EmailMessage()
     msg["to"]=email
     msg["from"]=gmail_cfg["email"]
     msg["subject"]="Send email with python"
     msg.set_content(message)

  #Create Smtp client, login to gmail and send the enail
     with smtplib.SMTP_SSL(gmail_cfg["server"],gmail_cfg["port"]) as smtp :
      smtp.login(gmail_cfg["email"],gmail_cfg["pwd"])
      smtp.send_message(msg)
     return  {"message": f"email send seccufully!!"}
    