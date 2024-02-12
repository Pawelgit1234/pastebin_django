from .models import Paste, Comment

from rest_framework import serializers


class PasteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paste
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'