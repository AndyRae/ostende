from django import forms
from tinymce import TinyMCE
from .models import Screening, Article


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScreeningUpdateForm(forms.ModelForm):
    class Meta:
        model = Screening
        fields = ['film', 'venue', 'season', 'programme', 'date', 'start_time', 
        'tickets', 'subtitle', 'copy', 'q_and_a', 'introduction', 'subtitled', 'audio_description',
        'relaxed_environment', 'dementia_friendly']
        widgets = {
            'date': DateInput(),
            'start_time': TimeInput(),
        }


class ArticleUploadForm(forms.ModelForm):
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
        widgets = {
            'date': DateInput(),
        }
