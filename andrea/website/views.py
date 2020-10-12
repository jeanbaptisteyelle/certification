from django.shortcuts import render
from . import models
from andreaapp import models as andreaapp_models
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
    info = models.InfoContact.objects.filter(status=True).last()
    siteinfo = models.Siteinfo.objects.filter(status=True)[:1].get()
    datas = {
        'siteinfo':siteinfo,
        'info':info
    }
    return render(request, 'pages/website/contact.html', datas)
