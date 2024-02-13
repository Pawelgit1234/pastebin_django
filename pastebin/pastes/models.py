from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from utils.slug import generate_hash


class Paste(models.Model):
	""" For texts, scripts, etc. """
	delete_options = [
		('SPECIFIC_DATE', 'Delete on specific date and time'),
		('AFTER_READ', 'Delete after read'),
		('NEVER', 'Never delete'),
	]

	PUBLIC = 'public'
	UNLISTED = 'unlisted'
	PRIVATE = 'private'

	PASTE_STATUS_CHOICES = [
		(PUBLIC, 'Public'),
		(UNLISTED, 'Unlisted'),
		(PRIVATE, 'Private'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pastes')
	title = models.CharField('Title', max_length=100)
	text = models.TextField('Text', max_length=10000)
	delete_option = models.CharField('Delete Option', choices=delete_options, default='NEVER', max_length=20)
	delete_at = models.DateTimeField('Delete At', blank=True, null=True)
	is_deactivated = models.BooleanField('Deactivated', default=False)
	status = models.CharField('Paste Status', choices=PASTE_STATUS_CHOICES, default=PUBLIC, max_length=20)
	slug = models.SlugField('Slug', max_length=10, blank=True)
	date = models.DateTimeField('Date and Time', default=timezone.now)

	def __str__(self):
		if bool(self.title):
			return self.title
		return self.text[:10]

	class Meta:
		db_table = "pastes"
		ordering = ['-date']
		verbose_name = "Paste"
		verbose_name_plural = "Pastes"

	def save(self, *args, **kwargs):
		if self.delete_option == 'NEVER':
			self.delete_at = None
		if not self.slug:
			hash_string = f"{self.user.username}-{self.text}-{timezone.now()}"
			self.slug = generate_hash(hash_string)[:10]
		super().save(*args, **kwargs)


class PasteView(models.Model):
	""" view from a paste """
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='views')
	paste = models.ForeignKey(Paste, on_delete=models.CASCADE, related_name='views')
	viewed_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('user', 'paste')


class Comment(models.Model):
	""" for commenting pastes """
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	paste = models.ForeignKey(Paste, on_delete=models.CASCADE, related_name='comments')
	text = models.TextField('Text', max_length=200)
	date = models.DateTimeField('Date and Time', default=timezone.now)
	reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

	def __str__(self):
		return self.text[:10]

	class Meta:
		db_table = "comments"
		ordering = ['-date']
		verbose_name = "Comment"
		verbose_name_plural = "Comments"
