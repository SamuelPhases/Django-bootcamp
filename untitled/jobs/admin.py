from django.contrib import admin

from blog.models import Blog
from .models import Job

# Register your models here.
admin.site.register(Job)
admin.site.register(Blog)