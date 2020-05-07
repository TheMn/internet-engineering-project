import os
from helli5 import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from .forms import reportForm
from .utils import create_zip
import hashlib

import csv
from django.http import HttpResponse
from django.contrib.auth.models import User


# def download_zip(request, assignment_id):
#     this_assignment = Homework.objects.get(id=assignment_id)
#     files = []
#     answers = Answers.objects.all()
#     for ans in answers:
#         if assignment_id == ans.homework.id:
#             files.append(ans.HW.url)
#             print("********** ", ans.HW.url)
#     print(create_zip(this_assignment, files))

def download_excel(request, course_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])
    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)
    return response


def courses(request):
    course_list = Course.objects.all()
    context = {
        'course_list': course_list
    }
    return render(request, 'courses.html', context)


def add_course(request):
    return render(request, 'add_course.html', {})


def course_single(request, course_id):
    this_course = get_object_or_404(Course, id=course_id)
    context = {
        'this_course': this_course
    }
    return render(request, 'course_single.html', context)


def homework(request, course_id, assignment_id):
    related_course = get_object_or_404(Course, id=course_id)
    this_assignment = get_object_or_404(Homework, id=assignment_id, course=related_course)
    context = {
        'this_assignment': this_assignment
    }
    return render(request, 'homework.html', context)


def upload_report(request):
    if request.user.has_perm('add_report'):
        if request.method == "POST":
            form = reportForm(request.POST, request.FILES)
            print(form.errors)
            if form.is_valid():
                files = request.FILES.getlist('files')
                directory = form.cleaned_data['report_title']

                report = Reports.objects.filter(title=directory)
                report = report.first()
                for file in files:
                    student_id = file.name.split('.')[0]
                    hashname = hashlib.md5(student_id.encode('utf-8')).hexdigest() + '.' + file.name.split('.')[1]
                    student_report = StudentReports()
                    student_report.report = report
                    student_report.student = student_id
                    student_report.report_url = '//' + settings.SITE_URL  + settings.MEDIA_URL + directory.split(' ')[0] + '/'\
                                                + hashname
                    student_report.save()
                    path = settings.MEDIA_ROOT + '\\reports\\' + directory.split(' ')[0]
                    if not os.path.isdir(path):
                        os.makedirs(path)
                    with open(path + '\\' + hashname, 'wb+') as destination:
                        for chunk in file.chunks():
                            destination.write(chunk)
                return redirect(upload_report)
            return HttpResponse(503)
        context = {
            'report': reportForm,
        }
        return render(request, 'report.html', context)
    return HttpResponse('Unauthorized', status=401)


def student_reports(request):
    user = request.user
    if user.is_authenticated:

        if user.profile.job_title == 'دانش آموز':
            report_students = StudentReports.objects.filter(student=user.username).all()
            reports = []
            for report_student in report_students:
                report = {
                    "name": report_student.report.title,
                    "link": report_student.report_url
                }
                reports.append(report)
            context = {
                'reports': reports,
            }
            return render(request, 'reports_page.html', context)
    else:
        return redirect('login')
