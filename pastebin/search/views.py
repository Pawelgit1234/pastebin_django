from django.shortcuts import render
from pastes.models import Paste


def search(request):
    query = request.GET.get('query')
    print("Query: ", query)
    pastes = Paste.objects.filter(status='public')
    if query:
        pastes = pastes.filter(title__icontains=query)
    return render(request, 'search/search_results.html', {'pastes': pastes, 'query': query})

