from django.http import HttpResponse
from django.shortcuts import render
from .forms import PageForm
from django.utils.timezone import now
from .models import PostStuff
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def blog_single(request):
    featured_posts = PostStuff.objects.filter(featured=True)[:5]
    context = {
        'featured_posts': featured_posts
    }
    return render(request, 'blog_single.html', context)


def add_post(request):
    form = PageForm
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.post_date = now()
            post.save()
            form = PageForm
    return render(request, 'add_post.html', {'form': form, })
