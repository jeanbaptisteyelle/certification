<<<<<<< HEAD
from django.shortcuts import render
from . import models
from andreaapp import models as andreaapp_models
=======
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from django.core.validators import validate_email
from andreaapp import models as andreaapp_models
from django.contrib.auth.models import User
>>>>>>> parent of 291c4f7... commit heroku
# Create your views here.
def index(request):
    fashion = andreaapp_models.Fashion.objects.filter(status=True).order_by('date_update')
    siteinfo = models.Siteinfo.objects.filter(status=True)[:1].get()
    datas = {
        'siteinfo':siteinfo,
        'fashion':fashion,
    }
    return render(request, 'pages/website/index.html', datas)

def contact(request):
<<<<<<< HEAD
=======
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)
        try:
            validate_email(email)
            if  email is not None and not name.isspace() and subject is not None and message is not None :
                contact = models.Contact(
                    name = name,
                    email = email,
                    subject = subject,
                    message = message,
                )
                contact.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"email incorect")
                
        except:
            messages.error(request, "veuillez entrer un email correct")
        return redirect(request.META.get('HTTP_REFERER', '/'))
  







>>>>>>> parent of 291c4f7... commit heroku
    info = models.InfoContact.objects.filter(status=True).last()
    siteinfo = models.Siteinfo.objects.filter(status=True)[:1].get()
    datas = {
        'siteinfo':siteinfo,
        'info':info
    }
    return render(request, 'pages/website/contact.html', datas)
<<<<<<< HEAD
=======


def newletter(request):
    if request.method=='POST':
        email = request.POST.get('email')
        print(email)
        try:
            validate_email(email)
            if  email is not None:
                letter = models.Newletter(
                    email = email,
                )
                letter.save()
                messages.success(request,"vos informations ont été enregistré")
            else:
                messages.error(request,"email incorect")
                
        except Exception as e:
            print(e)
            messages.error(request, "l'enregistrement à echoué")
    return redirect(request.META.get('HTTP_REFERER', '/'))
>>>>>>> parent of 291c4f7... commit heroku
