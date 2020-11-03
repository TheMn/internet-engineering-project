from django.shortcuts import render
from django.db.models import Q
from postingApp.models import PostStuff
from .models import Team, Pansouq, Transaction, Participant, Challenge


def students_list(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    print(challenge, '************************')
    context = {
        "challenge": challenge,
    }
    return render(request, 'pansouq_students_list.html', context)


def pansouq(request, pansouq_id):
    post_list = PostStuff.objects.filter(Q(categories__title__exact='پژوهشی')).distinct()[:3]
    teams_list = Team.objects.filter(related_pansouq_id=pansouq_id)
    pansouq = Pansouq.objects.get(id=pansouq_id)
    max_points = Transaction.get_max_points()
    for x in max_points:
        x['participant'] = Participant.objects.get(id=x['participant'])
    context = {
        'post_list': post_list,
        'teams_list': teams_list,
        'pansouq': pansouq,
        'max_points': max_points,
    }
    return render(request, 'pansouq.html', context)
