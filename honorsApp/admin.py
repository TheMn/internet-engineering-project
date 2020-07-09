from django.contrib import admin

from .models import *


@admin.register(Honors)
class HonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'title_2', 'period',)
    list_editable = ('title', 'title_2',)
    list_filter = ('period',)
    search_fields = ('name',)
# Register your models here.
# admin.site.register(Honors)
