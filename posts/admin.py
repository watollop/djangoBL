from django.contrib import admin

# Register your models here.

from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "update"]
    list_display_links = ["update"]
    list_filter =["timestamp"]
    search_fields = ["title"]
    list_editable =["title"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
