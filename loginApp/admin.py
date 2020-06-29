from django.contrib import admin
from loginApp.models import *
# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Profile)
admin.site.register(Role)

class ContactAdmin(admin.ModelAdmin):
    ordering = ['seen']
    # list_display_links = ['plate']
    list_display = ('date', 'subject', 'name', 'email', 'seen')
    list_filter = ('seen', 'date')

admin.site.register(Contact, ContactAdmin)
