from django.contrib import admin
from .models import User, Post, follow_status
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(follow_status)