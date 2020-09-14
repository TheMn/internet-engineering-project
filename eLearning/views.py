from django.shortcuts import render
from helli5.decorators import has_perm
import requests
import datetime
import xmltodict
from loginApp.models import User


@has_perm('check_classes')
def check_classes(request):
    classes = {
        '101': '99902',
        '102': '99981',
        '103': '100064',
        '111': '27475',
        '112': '27366',
        '121': '27590',
        '122': '27715'

    }
    start_times = {
        '1': '8:00:00',
        '2': '9:35:00',
        '3': '11:10:00',
        '4': '12:45:00'
    }
    end_times = {
        '1': '9:15:00',
        '2': '10:50:00',
        '3': '12:25:00',
        '4': '14:00:00'
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
            'https://online.allamehelli5.ir/api/xml?action=login&login=mahdighanbari@helli5.ir&password=mahdipass')
        breeze = response.cookies.get('BREEZESESSION')
        all_students = []
        if cls == '10':
            all_students = User.objects.filter(username__regex='99d*')
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                    '101') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
            response = response.content
            students = xmltodict.parse(response)
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                    '102') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
            response = response.content
            students.update(xmltodict.parse(response))
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                    '103') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
            response = response.content
            students.update(xmltodict.parse(response))
        elif cls == '11':
            all_students = User.objects.filter(username__regex='98d*').all()
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                    '111') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
            response = response.content
            students = xmltodict.parse(response)
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                    '112') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
            response = response.content
            students.update(xmltodict.parse(response))
        elif cls == '12':
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                    '121') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
            response = response.content
            students = xmltodict.parse(response)
            response = requests.get(
                'https://online.allamehelli5.ir/api/xml?action=report-meeting-attendance&sco-id=' + classes.get(
                    '122') + '&' + generate_date_query_param(zang_start, zang_end) + '&session=' + breeze)
            response = response.content
            students.update(xmltodict.parse(response))

        checks = {}
        emails = {}
        for student in students['results']['report-meeting-attendance']['row']:
            date_end = end_times[zang]
            if 'date-end' in student.keys():
                date_end = student['date-end']
            emails[student['login']] = {'time_in': student['date-created'], 'time_out': date_end}
        for student in all_students:
            if student.email in emails.keys():
                row = {'check': True, 'in': emails[student.email]['time_in'], 'out': emails[student.email]['time_out'],
                       'name': student.first_name + ' ' + student.last_name}
            else:
                row = {'check': False, 'name': student.first_name + ' ' + student.last_name}
            checks[student.email] = row
        context = {'response': checks}
        return render(request, 'pa_page.html', context)


def generate_date_query_param(start_time, end_time):
    date = datetime.date.today()
    year = date.year
    month = date.month
    day = date.day
    return 'filter-gt-date-created=' + str(year) + '-' + str(month) + '-' + str(
        day) + 'T' + start_time + '&filter-lt-date-created=' + str(year) + '-' + str(month) + '-' + str(
        day) + 'T' + end_time
