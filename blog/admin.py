# blog/admin.py

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on', 'updated_on', 'image_tag', 'video_link']
    search_fields = ['title', 'author__username']
    readonly_fields = ['created_on', 'updated_on', 'image_tag', 'video_link']

    fieldsets = [
        ('Post Information', {'fields': ['title', 'author', 'content']}),
        ('Media', {'fields': ['image', 'video']}),
        ('Timestamps', {'fields': ['created_on', 'updated_on'], 'classes': ['collapse']}),
    ]

    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-width:200px;max-height:200px;" />'
        return 'No Image'
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'

    def video_link(self, obj):
        if obj.video:
            return f'<a href="{obj.video.url}" target="_blank">View Video</a>'
        return 'No Video'
    video_link.allow_tags = True
    video_link.short_description = 'Video Link'

admin.site.register(Post, PostAdmin)
