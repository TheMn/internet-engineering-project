from django.contrib import admin
from .models import SliderContent


@admin.register(SliderContent)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'description', 'visible')
    search_fields = ('title',)
    list_filter = ('visible',)
    list_editable = ('title', 'description', 'visible')
