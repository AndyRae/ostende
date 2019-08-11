from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import Programme, Venue, Film, Season, Screening, Author, Article

admin.site.register(Programme)
admin.site.register(Venue)
admin.site.register(Film)
admin.site.register(Season)
admin.site.register(Author)
admin.site.register(Article)


# This is for the import/export
class ScreeningResource(resources.ModelResource):
    film = fields.Field(column_name='film', attribute='film', widget=ForeignKeyWidget(Film, field='name'))
    venue = fields.Field(column_name='venue', attribute='venue', widget=ForeignKeyWidget(Venue, field='name'))
    season = fields.Field(column_name='season', attribute='season', widget=ForeignKeyWidget(Season, field='name'))
    programme = fields.Field(column_name='programme', attribute='programme', widget=ForeignKeyWidget(Programme, field='name'))

    class Meta:
        film = fields.Field(
                column_name='film',
                attribute='film',
                widget=ForeignKeyWidget(Film, 'name'))
        model = Screening
        fields = ('id', 'name', 'date', 'start_time', 'tickets', 'film',
                'venue', 'season', 'programme', 'subtitle', 'q_and_a',)
        fields = ('id', 'film', 'venue', 'season', 'programme', 'date', 'start_time', 
                'tickets', 'subtitle', 'copy', 'q_and_a', 'introduction', 'subtitled', 'audio_description',
                'relaxed_environment', 'dementia_friendly')


class ScreeningAdmin(ImportExportModelAdmin):
    resource_class = ScreeningResource


admin.site.register(Screening, ScreeningAdmin)
