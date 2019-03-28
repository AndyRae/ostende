from rest_framework import serializers
from .models import Film, Venue, Screening


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class ScreeningSerializer(serializers.ModelSerializer):
    film = FilmSerializer()
    venue = VenueSerializer()

    class Meta:
        model = Screening
        fields = '__all__'
