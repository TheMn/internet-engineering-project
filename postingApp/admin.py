from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(PostStuff)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Attachment)
admin.site.register(Role)
admin.site.register(Category)
