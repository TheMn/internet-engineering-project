from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PageForm, CommentForm
from django.utils.timezone import now
from .models import PostStuff, Comment, Category, Profile
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
    categories = Category.objects.all()
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
        'categories': categories
        # 'archive_count': archive_count,
    }
    return render(request, 'blog.html', context)


def blog_single(request, slug):
    post = get_object_or_404(PostStuff, slug=slug)
    categories = Category.objects.all()
    featured_posts = PostStuff.objects.filter(featured=True)[:5]
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user.profile
            form.instance.post = post
            form.save()
            return redirect(reverse("blog_single", kwargs={
                'slug': post.pk
            }))
    context = {
        'comment_form': form,
        'featured_posts': featured_posts,
        'this_post': post,
        'categories': categories
    }
    return render(request, 'blog_single.html', context)


def get_author(user):
    qs = Profile.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def blog_update(request, slug):
    title = 'Update'
    post = get_object_or_404(PostStuff, slug=slug)
    form = PageForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user.profile)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("blog_single", kwargs={
                'slug': form.instance.slug
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'add_post.html', context)


def blog_delete(request, slug):
    post = get_object_or_404(PostStuff, slug=slug)
    post.delete()
    return redirect(reverse("blog"))


def add_post(request):
    form = PageForm
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = request.user.profile
            post.save()
            form = PageForm
    return render(request, 'add_post.html', {'form': form, })
