from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Homework)
admin.site.register(Answers)
admin.site.register(Course)
admin.site.register(Reports)
admin.site.register(StudentReports)
