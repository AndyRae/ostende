from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Venue, Film, Season, Screening, Programme, Article
from .forms import venueuploadform, filmuploadform, seasonuploadform, articleuploadform
from datetime import datetime


class VenueListView(ListView):
    model = Venue
    template_name = 'core/venues/venues.html'
    context_object_name = 'venues'
    ordering = ['name']
    paginate_by = 12


class VenueDetailView(DetailView):
    model = Venue
    template_name = 'core/venues/venue_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VenueDetailView, self).get_context_data(**kwargs)
        todaysdate = datetime.now().date()
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(venue_id=self.kwargs['pk']).filter(
            date__gte=todaysdate).order_by('date')[:6]
        context['pastscreenings'] = Screening.objects.filter(venue_id=self.kwargs['pk']).filter(
            date__lte=todaysdate).order_by('-date')[:3]
        return context


class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    fields = ['name', 'city', 'postcode',
              'county', 'website', 'twitter', 'facebook', 'image']
    template_name = 'core/venues/venue_form.html'


class VenueUpdateView(LoginRequiredMixin, UpdateView):
    model = Venue
    fields = ['name', 'city', 'postcode',
              'county', 'website', 'twitter', 'facebook', 'image']
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
    paginate_by = 12


class FilmDetailView(DetailView):
    model = Film
    template_name = 'core/films/film_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        todaysdate = datetime.now().date()
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(film_id=self.kwargs['pk']).filter(
            date__gte=todaysdate).order_by('date')
        context['pastscreenings'] = Screening.objects.filter(film_id=self.kwargs['pk']).filter(
            date__lte=todaysdate).order_by('-date')
        return context


class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film
    fields = ['name', 'director', 'cast', 'country',
              'year', 'certificate', 'length', 'copy', 'image']
    template_name = 'core/films/film_form.html'


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    fields = ['name', 'director', 'cast', 'country',
              'year', 'certificate', 'length', 'copy', 'image']
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
    paginate_by = 12


class SeasonDetailView(DetailView):
    model = Season
    template_name = 'core/seasons/season_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SeasonDetailView, self).get_context_data(**kwargs)
        todaysdate = datetime.now().date()
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(season_id=self.kwargs['pk']).filter(
            date__gte=todaysdate).order_by('date')[:6]
        context['pastscreenings'] = Screening.objects.filter(season_id=self.kwargs['pk']).filter(
            date__lte=todaysdate).order_by('-date')[:3]
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
    paginate_by = 12
    todaysdate = datetime.now().date()
    queryset = Screening.objects.filter(date__gte=todaysdate).order_by('date')


class ScreeningListingView(ListView):
    model = Screening
    template_name = 'core/screenings/screening_list.html'
    context_object_name = 'screenings'
    ordering = ['-date']


class ScreeningDateListingView(ListView):
    model = Screening
    template_name = 'core/screenings/thismonth.html'
    context_object_name = 'screenings'


class ScreeningDetailView(DetailView):
    model = Screening
    template_name = 'core/screenings/screening_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ScreeningDetailView, self).get_context_data(**kwargs)
        todaysdate = datetime.now().date()
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(
            date__gte=todaysdate).order_by('date')[:3]
        return context


class ScreeningCreateView(LoginRequiredMixin, CreateView):
    model = Screening
    fields = ['film', 'venue', 'season', 'date', 'start_time', 'tickets', 'subtitle', 'q_and_a']
    template_name = 'core/screenings/screening_form.html'


class ScreeningUpdateView(LoginRequiredMixin, UpdateView):
    model = Screening
    fields = ['film', 'venue', 'season', 'date', 'start_time', 'tickets', 'subtitle', 'q_and_a']
    template_name = 'core/screenings/screening_form.html'


class ScreeningDeleteView(LoginRequiredMixin, DeleteView):
    model = Screening
    success_url = '/'
    template_name = 'core/screenings/screening_confirm_delete.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'core/articles/articles.html'
    context_object_name = 'articles'
    ordering = ['-date']
    paginate_by = 12


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'core/articles/article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'date', 'author', 'programme', 'image', 'text']
    template_name = 'core/articles/article_form.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'date', 'author', 'programme', 'image', 'text']
    template_name = 'core/articles/article_form.html'


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
        # context['screenings'] = Screening.objects.all()
        context['articles'] = Article.objects.filter(
            date__lte=todaysdate).order_by('-date')[:2]
        return context
