from django.contrib import admin
from .models import PostStuff
from .models import Profile
from .models import Comment
from .models import Attachment
from .models import Role

# Register your models here.
admin.site.register(PostStuff)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Attachment)
admin.site.register(Role)
