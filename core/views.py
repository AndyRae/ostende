from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum, Q
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Home, Venue, Film, Season, Screening
from datetime import datetime


def home(request):
    return render(request, 'core/home.html')


class HomeView(ListView):
    model = Screening
    context_object_name = 'screenings'
    template_name = 'core/home.html'
    ordering = ['date']
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        todaysdate = datetime.now().date()
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(
            date__gte=todaysdate)
        return context


class VenueListView(ListView):
    model = Venue
    template_name = 'core/venues/venues.html'
    context_object_name = 'venues'
    ordering = ['name']
    paginate_by = 20


class VenueDetailView(DetailView):
    model = Venue
    template_name = 'core/venues/venue_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VenueDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(venue_id=self.kwargs['pk'])
        return context


class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    fields = ['name', 'address', 'postcode', 'county', 'website', 'twitter', 'facebook']
    template_name = 'core/venues/venue_form.html'


class VenueUpdateView(LoginRequiredMixin, UpdateView):
    model = Venue
    fields = ['name', 'address', 'postcode', 'county', 'website', 'twitter', 'facebook']
    template_name = 'core/venues/venue_form.html'


class VenueDeleteView(LoginRequiredMixin, DeleteView):
    model = Venue
    success_url = '/'
    template_name = 'core/films/film_confirm_delete.html'


class FilmListView(ListView):
    model = Film
    template_name = 'core/films/films.html'
    context_object_name = 'films'
    ordering = ['name']
    paginate_by = 20


class FilmDetailView(DetailView):
    model = Film
    template_name = 'core/films/film_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(film_id=self.kwargs['pk'])
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
    paginate_by = 20


class SeasonDetailView(DetailView):
    model = Season
    template_name = 'core/seasons/season_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SeasonDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet for all objects
        context['screenings'] = Screening.objects.filter(season_id=self.kwargs['pk'])
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
    paginate_by = 20


class ScreeningDetailView(DetailView):
    model = Screening
    template_name = 'core/screenings/screening_detail.html'


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
