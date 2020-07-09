from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

from .models import *


class PostStuffAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'username', 'date', 'featured')
    search_fields = ('title',)
    list_filter = ('featured',)


admin.site.register(PostStuff, PostStuffAdmin)


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('cm_date', 'author', 'post')
    list_filter = ('cm_date',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ordering = ['order']
    list_display = ('order', 'text', 'day',)
    list_editable = ('text', 'day',)
    list_filter = ('day',)
    search_fields = ('text',)


# admin.site.register(Comment)
# admin.site.register(Event)

admin.site.register(Attachment)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_honored')
    list_editable = ('is_honored',)
    list_filter = ('is_honored',)
    search_fields = ('title',)
# admin.site.register(Category)
