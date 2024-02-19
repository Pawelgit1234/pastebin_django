from django.contrib import admin
from .models import Paste, Comment


class PasteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'status', 'delete_option', 'views_count')
    list_filter = ('status', 'delete_option')
    search_fields = ('title', 'text')
    readonly_fields = ('date', 'views_count')
    date_hierarchy = 'date'

    def views_count(self, obj):
        return obj.views.count()

    views_count.short_description = 'Views'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'paste', 'text', 'date', 'reply_to')
    list_filter = ('date',)
    search_fields = ('text',)
    readonly_fields = ('date',)

admin.site.register(Paste, PasteAdmin)
admin.site.register(Comment, CommentAdmin)
