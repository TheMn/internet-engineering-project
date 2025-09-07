"""
Views for the posting app.

This module contains the views for the posting app, which handle displaying,
creating, updating, and deleting blog posts, as well as searching for posts and
handling comments.
"""
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

# def posts_by_cat(request, id):
#     cat = get_object_or_404(Category, id=id)
#     for mpost in cat.get_posts():
#         print(mpost.title)


def search(request):
    """
    Searches for blog posts.

    This view searches for blog posts that match the query provided in the
    'search' GET parameter. The search is performed on the title and text of
    the posts.

    Args:
        request: The HTTP request.

    Returns:
        The rendered search results page.
    """
    queryset = PostStuff.objects.all()
    query = request.GET.get('search')
    if query:
        queryset = queryset.filter(Q(title__icontains=query) |
                                   Q(text__icontains=query)
                                   ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)


# def modir(request):
#     q = PostStuff.objects.all()
#     tag = request.GET.get('tag')
#     if tag:
#         q = q.filter(Q(categories__title__exact =tag)).distinct()
#     context = {
#         'queryset': q
#     }
#     return render(request, 'search_results.html', context)


def blog(request, tag=None):
    """
    Renders the blog page.

    This view displays a paginated list of all blog posts. If a 'tag' is
    provided, it filters the posts by that tag.

    Args:
        request: The HTTP request.
        tag (str, optional): The tag to filter the posts by. Defaults to None.

    Returns:
        The rendered blog page.
    """
    categories = Category.objects.all()

    if tag:
        post_list = PostStuff.objects.filter(Q(categories__title__exact=tag)).distinct()
    else:
        post_list = PostStuff.objects.all()

    paginator = Paginator(post_list, 20)
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
        'categories': categories,
        'tagged_blog': tag if tag else 'None'
    }

    return render(request, 'blog.html', context)


def blog_single(request, slug):
    """
    Renders a single blog post page.

    This view displays a single blog post, identified by its slug. It also
    handles the submission of comments on the post.

    Args:
        request: The HTTP request.
        slug (str): The slug of the post.

    Returns:
        The rendered blog post page.
    """
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
                'slug': post.slug
            }))
    title = post.title + ' | وبسایت دبیرستان دوره دوم علامه حلی ۵ تهران'
    context = {
        'comment_form': form,
        'title':title,
        'featured_posts': featured_posts,
        'this_post': post,
        'categories': categories
    }
    return render(request, 'blog_single.html', context)


def get_author(user):
    """
    Gets the profile of a user.

    Args:
        user: The user object.

    Returns:
        The user's profile object, or None if it doesn't exist.
    """
    qs = Profile.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def blog_update(request, slug):
    """
    Handles the updating of a blog post.

    This view allows the author of a post to update its content.

    Args:
        request: The HTTP request.
        slug (str): The slug of the post to be updated.

    Returns:
        The rendered update post page.
    """
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
    """
    Handles the deletion of a blog post.

    This view allows the author of a post to delete it.

    Args:
        request: The HTTP request.
        slug (str): The slug of the post to be deleted.

    Returns:
        A redirect to the blog page.
    """
    post = get_object_or_404(PostStuff, slug=slug)
    post.delete()
    return redirect(reverse("blog"))


def add_post(request):
    """
    Handles the creation of a new blog post.

    Args:
        request: The HTTP request.

    Returns:
        The rendered add post page.
    """
    form = PageForm
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        print('***********')
        # 'title',
        # 'text',
        # 'description',
        # 'img',
        # 'featured',
        post = form.save(commit=False)
        post.username = request.user.profile
        post.title = request.POST['title']
        post.description = request.POST['description']
        print('~~~~~~~~~~>', post)
        post.save()
        form = PageForm
    return render(request, 'add_post.html', {'form': form, })

# def add_post_teacher(request):
#     return render(request, 'add_post_teacher.html', {})
