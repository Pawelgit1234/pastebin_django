from django.contrib import admin
from .models import Paste, Comment


class PasteAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'date', 'status', 'delete_option', 'views')
	list_filter = ('status', 'delete_option')
	search_fields = ('title', 'text')
	readonly_fields = ('date', 'views')
	date_hierarchy = 'date'


class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'paste', 'text', 'date', 'reply_to')
	list_filter = ('date',)
	search_fields = ('text',)
	readonly_fields = ('date',)

admin.site.register(Paste, PasteAdmin)
admin.site.register(Comment, CommentAdmin)