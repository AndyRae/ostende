"""ostende URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap
from .routers import router
from core.sitemaps import (
    VenueSitemap,
    FilmSitemap,
    SeasonSitemap,
    ScreeningSitemap,
    AuthorSitemap,
    ArticleSitemap,
)

sitemaps = {
    "venues": VenueSitemap,
    "films": FilmSitemap,
    "seasons": SeasonSitemap,
    "screenings": ScreeningSitemap,
    "authors": AuthorSitemap,
    "articles": ArticleSitemap,
}


urlpatterns = [
    path("member/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", include("core.urls")),
    path(r"tinymce/", include("tinymce.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("pages/", include("django.contrib.flatpages.urls")),
    path("about/", views.flatpage, {"url": "/about/"}, name="about"),
    path("privacy/", views.flatpage, {"url": "/privacy/"}, name="privacy"),
    path("profile/", user_views.profile, name="profile"),
    path(
        "enter/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "exit/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
]

handler404 = "core.views.handler404"
handler500 = "core.views.handler500"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
