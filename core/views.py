from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.http import HttpResponseRedirect
from .models import Venue, Film, Season, Screening, Article
from .forms import ScreeningUpdateForm, ArticleForm
from datetime import datetime


class VenueListView(ListView):
    model = Venue
    template_name = 'core/venues/venues.html'
    context_object_name = 'venues'
    ordering = ['name']
    paginate_by = 9


class VenueDetailView(DetailView, MultipleObjectMixin):
    model = Venue
    template_name = 'core/venues/venue_detail.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        todaysdate = datetime.now().date()
        object_list = Screening.objects.filter(venue_id=self.kwargs['pk']).filter(date__gte=todaysdate).order_by('date')
        context = super(VenueDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class VenueArchiveView(DetailView, MultipleObjectMixin):
    model = Venue
    template_name = 'core/venues/venue_archive.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        todaysdate = datetime.now().date()
        object_list = Screening.objects.filter(venue_id=self.kwargs['pk']).filter(date__lte=todaysdate).order_by('-date')
        context = super(VenueArchiveView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    fields = ['name', 'city', 'postcode',
              'county', 'website', 'twitter', 'facebook', 'copy', 'image']
    template_name = 'core/venues/venue_form.html'


class VenueUpdateView(LoginRequiredMixin, UpdateView):
    model = Venue
    fields = ['name', 'city', 'postcode',
              'county', 'website', 'twitter', 'facebook', 'copy', 'image']
    template_name = 'core/venues/venue_form.html'


class VenueDeleteView(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url = '/'
    template_name = 'core/venues/venue_confirm_delete.html'


class FilmListView(ListView):
    model = Film
    template_name = 'core/films/films.html'
    context_object_name = 'films'
    ordering = ['name']
    paginate_by = 9


class FilmDetailView(DetailView, MultipleObjectMixin):
    model = Film
    template_name = 'core/films/film_detail.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        todaysdate = datetime.now().date()
        object_list = Screening.objects.filter(film_id=self.kwargs['pk']).filter(date__gte=todaysdate).order_by('date')
        context = super(FilmDetailView, self).get_context_data(object_list=object_list, **kwargs)
        context['articles'] = Article.objects.filter(film_id=self.kwargs['pk'])
        return context


class FilmArchiveView(DetailView, MultipleObjectMixin):
    model = Film
    template_name = 'core/films/film_archive.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        todaysdate = datetime.now().date()
        object_list = Screening.objects.filter(film_id=self.kwargs['pk']).filter(date__lte=todaysdate).order_by('-date')
        context = super(FilmArchiveView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film
    fields = ['name', 'director', 'cast', 'country',
              'year', 'certificate', 'length', 'trailer', 'copy', 'quote', 'quote_source', 'image']
    template_name = 'core/films/film_form.html'


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    fields = ['name', 'director', 'cast', 'country',
              'year', 'certificate', 'length', 'trailer', 'copy', 'quote', 'quote_source', 'image']
    template_name = 'core/films/film_form.html'


class FilmDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    success_url = '/'
    template_name = 'core/films/film_confirm_delete.html'


class SeasonListView(ListView):
    model = Season
    template_name = 'core/seasons/seasons.html'
    context_object_name = 'seasons'
    ordering = ['name']
    paginate_by = 9


class SeasonDetailView(DetailView, MultipleObjectMixin):
    model = Season
    template_name = 'core/seasons/season_detail.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        todaysdate = datetime.now().date()
        object_list = Screening.objects.filter(season_id=self.kwargs['pk']).filter(date__gte=todaysdate).order_by('date')
        context = super(SeasonDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class SeasonArchiveView(DetailView, MultipleObjectMixin):
    model = Season
    template_name = 'core/seasons/season_archive.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        todaysdate = datetime.now().date()
        object_list = Screening.objects.filter(season_id=self.kwargs['pk']).filter(date__lte=todaysdate).order_by('-date')
        context = super(SeasonArchiveView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class SeasonCreateView(LoginRequiredMixin, CreateView):
    model = Season
    fields = ['name', 'copy', 'image']
    template_name = 'core/seasons/season_form.html'


class SeasonUpdateView(LoginRequiredMixin, UpdateView):
    model = Season
    fields = ['name', 'copy', 'image']
    template_name = 'core/seasons/season_form.html'


class SeasonDeleteView(LoginRequiredMixin, DeleteView):
    model = Season
    success_url = '/'
    template_name = 'core/seasons/season_confirm_delete.html'


class ScreeningListView(ListView):
    model = Screening
    template_name = 'core/screenings/screenings.html'
    context_object_name = 'screenings'
    ordering = ['date']
    paginate_by = 9
    todaysdate = datetime.now().date()
    queryset = Screening.objects.filter(date__gte=todaysdate).order_by('date')


class ScreeningListingView(LoginRequiredMixin, ListView):
    model = Screening
    template_name = 'core/screenings/screening_list.html'
    context_object_name = 'screenings'
    ordering = ['-date']
    paginate_by = 100


class ScreeningDateListingView(ListView):
    model = Screening
    template_name = 'core/screenings/thismonth.html'
    context_object_name = 'screenings'


class ScreeningDetailView(DetailView, MultipleObjectMixin):
    model = Screening
    template_name = 'core/screenings/screening_detail.html'

    def get_context_data(self, **kwargs):
        todaysdate = datetime.now().date()
        object_list = Screening.objects.filter(date__gte=todaysdate).order_by('date')[:3]
        context = super(ScreeningDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class ScreeningCreateView(LoginRequiredMixin, CreateView):
    model = Screening
    template_name = 'core/screenings/screening_form.html'
    form_class = ScreeningUpdateForm
    success_url = '/'


class ScreeningUpdateView(LoginRequiredMixin, UpdateView):
    model = Screening
    template_name = 'core/screenings/screening_form.html'
    form_class = ScreeningUpdateForm
    success_url = '/'


class ScreeningDeleteView(LoginRequiredMixin, DeleteView):
    model = Screening
    success_url = '/'
    template_name = 'core/screenings/screening_confirm_delete.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'core/articles/articles.html'
    context_object_name = 'articles'
    ordering = ['-date']
    paginate_by = 9

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        todaysdate = datetime.now().date()
        # Add in a QuerySet for all objects
        context['articles'] = Article.objects.filter(date__lte=todaysdate).order_by('-date')
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'core/articles/article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'core/articles/article_form.html'
    form_class = ArticleForm


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'core/articles/article_form.html'
    form_class = ArticleForm


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url = '/'
    template_name = 'core/articles/article_confirm_delete.html'


class HomeView(ListView):
    model = Screening
    context_object_name = 'screenings'
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        todaysdate = datetime.now().date()
        # Add in a QuerySet for all objects
        context['articles'] = Article.objects.filter(date__lte=todaysdate).order_by('-date')
        return context


def handler404(request, *args, **kwargs):
    response = render(request, "core/404.html", status=404)
    return response


def handler500(request, *args, **kwargs):
    response = render(request, "core/404.html", status=500)
    return response
