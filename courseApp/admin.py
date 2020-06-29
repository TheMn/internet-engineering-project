from django.contrib import admin

from .models import *


@admin.register(Reports)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(StudentReports)
class StudentReportAdmin(admin.ModelAdmin):
    list_display = ('student', 'report',)
    list_filter = ('report',)
    search_fields = ('student',)


# Register your models here.
admin.site.register(Homework)
admin.site.register(Answers)
admin.site.register(Course)
# admin.site.register(Reports, ReportAdmin)
# admin.site.register(StudentReports)
