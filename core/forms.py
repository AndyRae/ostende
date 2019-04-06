from django import forms
from tinymce import TinyMCE
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


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class ArticleForm(forms.ModelForm):
    text = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
