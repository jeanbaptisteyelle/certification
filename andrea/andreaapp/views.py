from django.shortcuts import render, redirect, get_object_or_404
from website import models as website_models
from . import models

 
# Create your views here.
def fashion(request):
<<<<<<< HEAD

    fashion = models.Fashion.objects.filter(status=True).order_by('date_update')
    siteinfo = website_models.Siteinfo.objects.filter(status=True)[:1].get()
    datas = {
        'fashion':fashion[:12],
        'siteinfo':siteinfo,
=======
    fashion = models.Fashion.objects.filter(status=True).order_by('-date_update')
    siteinfo = website_models.Siteinfo.objects.filter(status=True)[:1].get()

   
    datas = {
        
        'fashion':fashion,
        'siteinfo':siteinfo,
       
>>>>>>> parent of 291c4f7... commit heroku
    }
    return render(request, 'pages/andrea/fashion.html', datas)

def travel(request):
    siteinfo = website_models.Siteinfo.objects.filter(status=True)[:1].get()
    travel = models.Travel.objects.filter(status=True).order_by('date_update')
    recent = models.Travel.objects.filter(status=True).order_by('-date_update')
    datas= {
        'travel':travel,
        'recent':recent[:3],
        'siteinfo':siteinfo,
    }
    return render(request, 'pages/andrea/travel.html', datas)

def about(request):
    siteinfo = website_models.Siteinfo.objects.filter(status=True)[:1].get()
    about = models.About.objects.filter(status=True).last()
    datas= {
        'about':about,
        'siteinfo':siteinfo,

    }
    return render(request, 'pages/andrea/about.html', datas)

def single(request, slug):
    article = models.Fashion.objects.get(slug=slug)
    siteinfo = website_models.Siteinfo.objects.filter(status=True)[:1].get()
<<<<<<< HEAD
    datas= {
        'siteinfo':siteinfo,
        'article':article,

    }
    return render(request, 'pages/andrea/single.html', datas)
=======
    single_article = get_object_or_404(models.Fashion, slug=slug)
    categories = models.Fashion.objects.filter(status=True)
    popular = models.Fashion.objects.filter(status=True)
    datas= {
        'siteinfo':siteinfo,
        'article':article,
        'single_article':single_article,
        'categories':categories,
        'popular':popular[:3]

    }
    return render(request, 'pages/andrea/single.html', datas)


>>>>>>> parent of 291c4f7... commit heroku
