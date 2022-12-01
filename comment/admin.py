from django.contrib import admin
from .models import Comment,Nested_Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Nested_Comment)
