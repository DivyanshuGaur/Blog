from django.contrib import admin
from . models import Author , Post , Tag,Comment
# Register your models here.



admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)