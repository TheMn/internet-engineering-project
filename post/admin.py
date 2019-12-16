from django.contrib import admin
from .models import PostStuff

from .models import Comment
from .models import Attachment
from .models import Role
from .models import Profile

# Register your models here.
admin.site.register(PostStuff)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Attachment)
admin.site.register(Role)
