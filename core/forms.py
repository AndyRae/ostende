from django import forms
from .models import Venue, Film, Season, Article


class venueuploadform(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('image',)


class filmuploadform(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('image',)


class seasonuploadform(forms.ModelForm):
    class Meta:
        model = Season
        fields = ('image',)


class articleuploadform(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('image',)
