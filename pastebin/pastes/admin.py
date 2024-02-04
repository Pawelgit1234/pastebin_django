from django.contrib import admin
from .models import Paste


class PasteAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'date', 'status', 'delete_option', 'views')
	list_filter = ('status', 'delete_option')
	search_fields = ('title', 'text')
	readonly_fields = ('date', 'views')
	date_hierarchy = 'date'

admin.site.register(Paste, PasteAdmin)
