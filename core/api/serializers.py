from rest_framework import serializers
from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from core.models import Film, Venue, Screening


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = 'id', 'name', 'director', 'certificate', 'image', 'slug'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = 'id', 'name', 'city', 'county', 'slug'


class ScreeningSerializer(serializers.ModelSerializer):
    film = FilmSerializer()
    venue = VenueSerializer()

    class Meta:
        model = Screening
        fields = 'id', 'name', 'date', 'start_time', 'tickets', 'film', 'venue'
