from django.contrib import admin
from .models import Post, Comment, User, Profile

# Register your models here.

from .models import Post

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)