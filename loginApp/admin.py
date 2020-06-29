from django.contrib import admin
from loginApp.models import *

# Register your models here.
admin.site.register(Subscriber)


# admin.site.register(Profile)
# admin.site.register(Role)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('person', 'role_s_')
    search_fields = ('person', 'role_s_')

    def role_s_(self, role_object):
        roles = []
        if role_object.is_teacher:
            roles.append('معلم')
        if role_object.is_student:
            roles.append('دانش آموز')
        if role_object.is_consulter:
            roles.append('مشاور')
        if role_object.is_moavenP:
            roles.append('معاون پژوهشی')
        if role_object.is_moavenO:
            roles.append('معاون المپیاد')
        if role_object.is_moavenE:
            roles.append('معاون آموزشی')
        if role_object.is_parent:
            roles.append('ولی')
        if role_object.is_principle:
            roles.append('مدیر')
        return ', '.join(roles)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'grade', 'group',)
    list_filter = ('grade', 'group',)
    search_fields = ('user',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = ['seen']
    # list_display_links = ['plate']
    list_display = ('date', 'subject', 'name', 'email', 'seen')
    list_filter = ('seen', 'date')

# admin.site.register(Contact, ContactAdmin)
