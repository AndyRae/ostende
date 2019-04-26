from django.urls import path
from .views import (
    HomeView,
    VenueListView,
    VenueDetailView,
    VenueCreateView,
    VenueUpdateView,
    VenueDeleteView,
    FilmListView,
    FilmDetailView,
    FilmCreateView,
    FilmUpdateView,
    FilmDeleteView,
    SeasonListView,
    SeasonDetailView,
    SeasonCreateView,
    SeasonUpdateView,
    SeasonDeleteView,
    ScreeningListView,
    ScreeningListingView,
    ScreeningDateListingView,
    ScreeningDetailView,
    ScreeningCreateView,
    ScreeningUpdateView,
    ScreeningDeleteView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('venues/', VenueListView.as_view(), name='venues'),
    path('venues/<str:slug>/<int:pk>/',
         VenueDetailView.as_view(), name='venue-detail'),
    path('venues/new/',
         VenueCreateView.as_view(), name='venue-create'),
    path('venues/<str:slug>/<int:pk>/update/',
         VenueUpdateView.as_view(), name='venue-update'),
    path('venues/<str:slug>/<int:pk>/delete/',
         VenueDeleteView.as_view(), name='venue-delete'),

    path('films/', FilmListView.as_view(), name='films'),
    path('films/<str:slug>/<int:pk>/',
         FilmDetailView.as_view(), name='film-detail'),
    path('films/new/',
         FilmCreateView.as_view(), name='film-create'),
    path('films/<str:slug>/<int:pk>/update/',
         FilmUpdateView.as_view(), name='film-update'),
    path('films/<str:slug>/<int:pk>/delete/',
         FilmDeleteView.as_view(), name='film-delete'),

    path('seasons/', SeasonListView.as_view(), name='seasons'),
    path('seasons/<str:slug>/<int:pk>/',
         SeasonDetailView.as_view(), name='season-detail'),
    path('seasons/new/',
         SeasonCreateView.as_view(), name='season-create'),
    path('seasons/<str:slug>/<int:pk>/update/',
         SeasonUpdateView.as_view(), name='season-update'),
    path('seasons/<str:slug>/<int:pk>/delete/',
         SeasonDeleteView.as_view(), name='season-delete'),

    path('screenings/', ScreeningListView.as_view(), name='screenings'),
    path('screenings/thismonth/', ScreeningDateListingView.as_view(), name='screening-month'),
    path('screenings/screening_list/', ScreeningListingView.as_view(), name='screening-list'),
    path('screenings/<int:pk>/',
         ScreeningDetailView.as_view(), name='screening-detail'),
    path('screenings/new/',
         ScreeningCreateView.as_view(), name='screening-create'),
    path('screenings/<int:pk>/update/',
         ScreeningUpdateView.as_view(), name='screening-update'),
    path('screenings/<int:pk>/delete/',
         ScreeningDeleteView.as_view(), name='screening-delete'),

    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<str:slug>/<int:pk>/',
         ArticleDetailView.as_view(), name='article-detail'),
    path('articles/new/',
         ArticleCreateView.as_view(), name='article-create'),
    path('articles/<str:slug>/<int:pk>/update/',
         ArticleUpdateView.as_view(), name='article-update'),
    path('articles/<str:slug>/<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article-delete'),
]
