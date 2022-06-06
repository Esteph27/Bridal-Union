from django.contrib import admin
from .models import Designer, ImagePosts, ImageComments


admin.site.register(Designer)

@admin.register(ImagePosts)
class ImagePostsAdmin(admin.ModelAdmin):

    list_display = ('image_name', 'date_posted', 'designer')
    list_filter = ('status', 'date_posted')
    prepopulated_fields = {'slug': ('image_name',)}
    search_fields = ('image_name', 'date_posted')


@admin.register(ImageComments)
class ImageCommentsAdmin(admin.ModelAdmin):

    list_display = ('user', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    action = ['approve_comments']

    def approved_comment(self, request, queryset):
        queryset.update(approved=True)

