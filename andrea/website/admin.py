from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Siteinfo)
class SiteinfoAdmin(admin.ModelAdmin):
    list_display  = ('copyrights','date_add','date_update','status','logo_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('copyrights',)
    date_hierarchy = 'date_add'
    list_display_links = ['copyrights']
    fieldsets = [
          ('Siteinfo_info', {'fields':['copyrights','logo']}),
          ('standard', {'fields':['status']}),
          ]
    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display  = ('email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    fieldsets = [
          ('Newletter_info', {'fields':['email']}),
          ('standard', {'fields':['status']}),
    ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.InfoContact)
class InfoContactAdmin(admin.ModelAdmin):
    list_display  = ('address','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('address',)
    date_hierarchy = 'date_add'
    list_display_links = ['address']
    fieldsets = [
          ('InfoContact_info', {'fields':['address','phone','email','website','marp_url']}),
          ('standard', {'fields':['status']}),
    ]
    
    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display  = ('name','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('name',)
    date_hierarchy = 'date_add'
    list_display_links = ['name']
    fieldsets = [
          ('Contact_info', {'fields':['name','email','subject','message']}),
          ('standard', {'fields':['status']}),
    ]
    
    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'