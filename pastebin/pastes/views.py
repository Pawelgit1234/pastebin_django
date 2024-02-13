from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from .models import Paste, PasteView, Comment


def home(request):
	pastes = get_list_or_404(Paste)
	return render(request, 'paste/home.html', {'pastes': pastes})


@login_required()
def detail(request, slug):
	paste = get_object_or_404(Paste, slug=slug)
	if not PasteView.objects.filter(user=request.user, paste=paste).exists():
		PasteView.objects.create(user=request.user, paste=paste)

	return render(request, "paste/detail.html", {"paste": paste})