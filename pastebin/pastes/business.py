from .models import Paste


def increment_views(slug: str) -> None:
    """ add a view to a paste """
    paste = Paste.objects.get(slug=slug)
    paste.views += 1
    paste.save(update_fields=['views'])