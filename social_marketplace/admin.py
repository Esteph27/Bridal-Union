from django.contrib import admin
from .models import *


admin.site.register(Designer)
admin.site.register(ImagePosts)
admin.site.register(ImageComments)
admin.site.register(CustomerAccount)
admin.site.register(Booking)


# @admin.register(Designer)
# class DesignerAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'location')
#     search_fields = ['first_name', 'last_name']
