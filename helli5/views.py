from django.template import loader
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from postingApp.models import PostStuff
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    latest = PostStuff.objects.order_by('-date')[0:3]
    context = {
        'latest_posts': latest
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def honors(request):
    return render(request, 'honors.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    post_list = PostStuff.objects.all()
    paginator = Paginator(post_list, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,

    }
    return render(request, 'blog.html', context)


def honors_card(request):
    return render(request, 'honors_card.html', {})


def courses(request):
    return render(request, 'courses.html', {})


def example(request):
    return render(request, 'example.html', {})


def base(request):
    return render(request, 'base.html', {})


def teacher(request):
    return render(request, 'teacher.html', {})


def blog_single(request):
    return render(request, 'blog-single.html', {})


def login(request):
    return render(request, 'login.html', {})

# def home(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
#
# def home(request):
#
#     template = loader.get_template('index.html')
#
#     return HttpResponse(template.render(request, {}))
