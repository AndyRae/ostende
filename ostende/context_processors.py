from django.conf import settings


def google_analytics(request):
    return {"google_analytics": settings.GOOGLE_ANALYTICS}


def title(request):
    return {"title": settings.TITLE}


def description(request):
    return {"description": settings.DESCRIPTION}


def twitter(request):
    return {"twitter": settings.TWITTER}
