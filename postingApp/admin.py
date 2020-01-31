from django.contrib import admin
from jalali_date import datetime2jalali

from .models import *
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

#
# # Register your models here.
# admin.site.register(PostStuff, AdminPosting)

@admin.register(PostStuff, Event)
class AdminPosting(ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    # list_display = ['some_fields', 'get_created_jalali']
    #
    # inlines = (MyInlines1, MyInlines2,)
    # raw_id_fields = ('some_fields',)
    # readonly_fields = ('some_fields', 'date_field',)
    # you can override formfield, for example:
    # formfield_overrides = {
    #     JSONField: {'widget': JSONEditor},
    # }

    # def get_created_jalali(self, obj):
    #     return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    # get_created_jalali.short_description = 'تاریخ ایجاد'
    # get_created_jalali.admin_order_field = 'created'

    exclude = ('slug',)

# class AdminPosting(admin.ModelAdmin):
#     exclude = ('slug',)


admin.site.register(Comment)

admin.site.register(Attachment)

admin.site.register(Category)
