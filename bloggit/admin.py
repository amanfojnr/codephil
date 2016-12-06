from django.contrib import admin
from .models import Post,Comment

# Register your models here.

# customize first before
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'publish','updated', 'status')
    list_filter = ('created', 'publish', 'status')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierachy = 'publish',
    ordering = ('status', 'publish')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'publish')
    list_filter = ('created')
    search_fields = ('author', 'content')
    raw_id_fields = ('author',)

admin.site.register(Post)
admin.site.register(Comment)
