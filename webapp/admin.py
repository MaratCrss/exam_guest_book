from django.contrib import admin

# Register your models here.
from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'email_author', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['title']
    search_fields = ['title', 'status']
    fields = ['title', 'email_author', 'status', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(GuestBook, GuestBookAdmin)