from django.http import HttpResponse
from django.shortcuts import render
from .forms import PageForm, CommentForm
from django.utils.timezone import now
from .models import PostStuff, Comment
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Extract
from django.db.models import Count, Q


# def get_archive_count():
#     #months = PostStuff.objects.annotate(month_stamp=Extract('time_stamp', 'month')).values_list('month_stamp', flat=True)
#     queryset = PostStuff.objects.values('date').annotate(Count('d'))
#
#     return months

def search(request):
    queryset = PostStuff.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(title__icontains=query) |
                                   Q(text__icontains=query)
                                   ).distinct()
        context = {
            'queryset': queryset
        }
        return render(request, 'search_results.html', context)


def blog(request):
    # archive_count = get_archive_count()
    # print(archive_count)
    post_list = PostStuff.objects.all()
    paginator = Paginator(post_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    featured_posts = PostStuff.objects.filter(featured=True)[:5]
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'featured_posts': featured_posts,
        # 'archive_count': archive_count,
    }
    return render(request, 'blog.html', context)


def blog_single(request, id):
    post = get_object_or_404(PostStuff, id=id)
    featured_posts = PostStuff.objects.filter(featured=True)[:5]
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user.profile
            form.instance.post = post
            form.save()
    context = {
        'comment_form': form,
        'featured_posts': featured_posts,
        'this_post': post
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
