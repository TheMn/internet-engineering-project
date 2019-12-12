from django.contrib import admin
from .models import PostStuff
from .models import User
from .models import Comment
from .models import Attachment
# Register your models here.
admin.site.register(PostStuff)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Attachment)