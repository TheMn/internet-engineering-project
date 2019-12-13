from django.http import HttpResponse
from django.shortcuts import render
from .forms import PageForm
from django.utils.timezone import now


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def make_post(request):
    form = PageForm
    if request.method == 'POST' :
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.post_date = now()
            post.save()
            form = PageForm
    return render(request, 'add_post.html', {'form': form,})