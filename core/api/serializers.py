from rest_framework import serializers
from core.models import Film, Venue, Screening
from rest_framework.serializers import ImageField


class FilmSerializer(serializers.ModelSerializer):
    image_thumbnail = ImageField(read_only=True)

    class Meta:
        model = Film
        fields = "id", "name", "director", "certificate", "image_thumbnail", "slug"


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = "id", "name", "city", "county", "slug"


class ScreeningSerializer(serializers.ModelSerializer):
    film = FilmSerializer()
    venue = VenueSerializer()

    class Meta:
        model = Screening
        fields = (
            "id",
            "name",
            "subtitle",
            "date",
            "start_time",
            "tickets",
            "film",
            "venue",
        )
