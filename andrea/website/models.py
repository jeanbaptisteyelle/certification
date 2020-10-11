from django.db import models

# Create your models here.
class Siteinfo(models.Model):
    logo = models.ImageField(upload_to='image/siteinfo')
    copyrights = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Siteinfo"
        verbose_name_plural = "Siteinfos"

    def __str__(self):
        return self.copyrights


class Newletter(models.Model):
    email = models.EmailField(max_length=254)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Newletter"
        verbose_name_plural = "Newletter"

    def __str__(self):
        return str(self.email)

class InfoContact(models.Model):
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=50)
    marp_url = models.TextField(null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "InfoContact"
        verbose_name_plural = "InfoContacts"

    def __str__(self):
        return self.address

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name






