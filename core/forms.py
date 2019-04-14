from django import forms
from tinymce import TinyMCE
from .models import Venue, Film, Season, Article, Screening


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


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


class screeningupdateform(forms.ModelForm):
    class Meta:
        model = Screening
        fields = ['film', 'venue', 'season', 'date', 'start_time', 'tickets', 'subtitle', 'q_and_a']
        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(),
        }


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
