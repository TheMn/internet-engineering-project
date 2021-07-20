from django.shortcuts import render
from helli5.decorators import has_perm
import requests
import datetime
import xmltodict
from loginApp.models import User


@has_perm('loginApp.check_classes')
def check_classes(request):
    try:
        classes = {
            '10R': '30634',
            '10M': '30520',
            '103': '30743',
            '111': '29901',
            '112': '30072',
            '11m': '30237',
            '121': '28443',
            '122': '28466',
            'zaA': '93411',
            'zaB': '93463',
            'zaC': '93515',
            '12m': '29355',
            'webinar': '29501'

        }
        start_times = {
            '1': '8:00:00',
            '2': '9:30:00',
            '3': '10:50:00',
            '4': '12:10:00'
        }
        end_times = {
            '1': '9:35:00',
            '2': '10:55:00',
            '3': '12:15:00',
            '4': '13:35:00'
        }
        zang = request.GET.get('zang')
        cls = request.GET.get('class')
        if zang is None or cls is None:
            context = {}
            return render(request, 'pa_page.html', context)
        else:
            students = {}
            zang_start = start_times.get(zang)
            zang_end = end_times.get(zang)
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=login&login=soroushsharify@gmail.com&password=4wmr4wmr')
            breeze = response.cookies.get('BREEZESESSION')
            all_students = []
            adobe_students = []
            if cls == '11':
                adobe_students = []
                all_students = User.objects.filter(username__regex='3995d*')
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '111') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = []
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '11m') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '112') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
            elif cls == '12':
                adobe_students = []
                all_students = User.objects.filter(username__regex='398d*').all()
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '121') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = []
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '122') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '12m') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
            elif cls == '10':
                adobe_students = []
                all_students = User.objects.filter(username__regex='999d*').all()
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '10R') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = []
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '103') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        '10M') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
            elif cls == 'zaban':
                adobe_students = []
                all_students = User.objects.filter(username__regex='98d*').all()
                all_students = all_students | User.objects.filter(username__regex='99d*').all()
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        'zaA') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = []
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        'zaB') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        'zaC') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                tmp = adobe_students
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = tmp
            elif cls == 'webinar':
                adobe_students = []
                all_students = User.objects.filter(username__regex='[0-9]d*').all()
                response = requests.get(
                    'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                        'webinar') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
                try:
                    response = response.content
                    students = xmltodict.parse(response)
                    adobe_students.append(students)
                except Exception:
                    adobe_students = []

            checks = {}
            emails = {}
            for adobe_student in adobe_students:
                if adobe_student['results']['report-meeting-attendance'] is not None:
                    for student in adobe_student['results']['report-meeting-attendance']['row']:
                        if isinstance(student, dict):
                            date_end = 'todayT' + end_times[zang] + '.'  # to do split with "T" character
                            if 'date-end' in student.keys():
                                date_end = student['date-end']
                            if 'login' in student.keys():
                                emails[student['login']] = {'time_in': student['date-created'], 'time_out': date_end}
            for student in all_students:
                if student.email in emails.keys():
                    row = {'check': True,
                           'in': datetime.datetime.strptime(
                               emails[student.email]['time_in'].split('T')[1].split('.')[0],
                               '%H:%M:%S'),
                           'out': datetime.datetime.strptime(
                               emails[student.email]['time_out'].split('T')[1].split('.')[0],
                               '%H:%M:%S'),
                           'name': student.first_name + ' ' + student.last_name,
                           'id': student.username,
                           'mom_phone': student.profile.mom_number,
                           'student_phone': student.profile.phone}
                else:
                    row = {'check': False,
                           'name': student.first_name + ' ' + student.last_name,
                           'id': student.username,
                           'mom_phone': student.profile.mom_number,
                           'student_phone': student.profile.phone}
                checks[student.email] = row
            context = {'response': checks}
            return render(request, 'pa_page.html', context)
    except Exception:
        context = {}
        return render(request, 'pa_page.html', context)


def generate_date_query_param(start_time, end_time):
    date = datetime.date.today()  # - datetime.timedelta(days=1)  # TODO: reset this
    year = date.year
    month = date.month
    day = date.day
    if day % 10 == day:
        day = '0' + str(day)
    if month % 10 == month:
        month = '0' + str(month)
    return 'filter-gt-date-created=' + str(year) + '-' + str(month) + '-' + str(
        day) + 'T' + start_time + '&filter-lt-date-created=' + str(year) + '-' + str(month) + '-' + str(
        day) + 'T' + end_time


def elearning_stuff(request):
    return render(request, 'elearning_stuff.html', {})
