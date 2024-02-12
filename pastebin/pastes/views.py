from django.shortcuts import render, get_object_or_404, get_list_or_404

from .business import increment_views
from .models import Paste, Comment


def home(request):
	pastes = get_list_or_404(Paste)
	return render(request, 'paste/home.html', {'pastes': pastes})


def detail(request, slug):
	paste = get_object_or_404(Paste, slug=slug)
	increment_views(slug) # TODO: one user can give just one view
	return render(request, "paste/detail.html", {"paste": paste})