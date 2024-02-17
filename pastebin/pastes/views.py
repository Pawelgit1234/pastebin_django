from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Paste, PasteView, Comment


def home(request):
	pastes = get_list_or_404(Paste)
	return render(request, 'paste/home.html', {'pastes': pastes})


def detail(request, slug):
	paste = get_object_or_404(Paste, slug=slug)
	if request.user.is_authenticated:
		if not PasteView.objects.filter(user=request.user, paste=paste).exists():
			PasteView.objects.create(user=request.user, paste=paste)

	return render(request, "paste/detail.html", {"paste": paste})