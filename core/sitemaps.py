from django.contrib.sitemaps import Sitemap
from .models import Venue, Film, Season, Screening, Author, Article


class VenueSitemap(Sitemap):
    def items(self):
        return Venue.objects.all()


class FilmSitemap(Sitemap):
    def items(self):
        return Film.objects.all()


class SeasonSitemap(Sitemap):
    def items(self):
        return Season.objects.all()


class ScreeningSitemap(Sitemap):
    def items(self):
        return Screening.objects.all()


class AuthorSitemap(Sitemap):
    def items(self):
        return Author.objects.all()


class ArticleSitemap(Sitemap):
    def items(self):
        return Article.objects.all()
