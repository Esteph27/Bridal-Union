from django.contrib import admin
from .models import Designer

# admin.site.register(Designer)


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    pass
