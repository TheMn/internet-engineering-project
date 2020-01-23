from django.contrib import admin

from .models import *


class AdminPosting(admin.ModelAdmin):
    exclude = ('slug',)


# Register your models here.
admin.site.register(PostStuff, AdminPosting)
admin.site.register(Comment)

admin.site.register(Attachment)

admin.site.register(Category)
