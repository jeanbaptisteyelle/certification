from django.db import models
<<<<<<< HEAD
from django.utils.text import slugify 
import time
zips = time.time()
=======
from django.contrib.auth.models import User
from django.utils.text import slugify 
import time
zips = time.time()
from tinymce import HTMLField
>>>>>>> parent of 291c4f7... commit heroku
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nom


class Fashion(models.Model):
    image = models.ImageField(upload_to='image/fashion')
    titre = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, related_name='categorieFashion', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='tagFashion')
<<<<<<< HEAD
=======
    content = HTMLField('content', null=True)
    created_by = models.ForeignKey(User, related_name='user' ,on_delete=models.CASCADE, null=True)
   
>>>>>>> parent of 291c4f7... commit heroku
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null= True, blank=True)

    def save(self, *args, **kwargs):
        self.slug ='-'.join((slugify(self.titre), (slugify(zips))))
        super(Fashion, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = "Fashion"
        verbose_name_plural = "Fashions"

    def __str__(self):
        return self.titre

class Travel(models.Model):
    image = models.ImageField(upload_to='image/travel')
    titre = models.CharField(max_length=255)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Travel"
        verbose_name_plural = "Travels"

    def __str__(self):
        return self.titre

   
class About(models.Model):
    background = models.ImageField(upload_to='background/about')
    titre = models.CharField(max_length=255)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.titre
