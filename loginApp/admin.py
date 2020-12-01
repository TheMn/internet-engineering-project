from django.contrib import admin
from loginApp.models import *

# Register your models here.
admin.site.register(Subscriber)


# admin.site.register(Profile)
# admin.site.register(Role)

@admin.register(PreRegisteredStudent)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display = ('melli_code', 'student_first_name', 'student_last_name', 'father_first_name')
    list_filter = ('field_of_study', 'is_valid')
    search_fields = ('student_first_name', 'student_last_name', 'melli_code')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'grade', 'group', 'financial_problem',)
    list_filter = ('grade', 'group',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = ['seen']
    # list_display_links = ['plate']
    list_display = ('date', 'subject', 'name', 'email', 'seen')
    list_filter = ('seen', 'date')

# admin.site.register(Contact, ContactAdmin)
