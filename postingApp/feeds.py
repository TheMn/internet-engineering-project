from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import PostStuff
from django.urls import reverse


class LatestPostsFeed(Feed):
    title = "دبیرستان علامه حلی ۵ تهران"
    link = "http://allamehelli5.ir/"
    description = "وبسایت دبیرستان پسرانه ی تیزهوشان دوره دوم علامه حلی ۵ تهران (سمپاد)"

    def items(self):
        return PostStuff.objects.filter(featured=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.description, 30)
