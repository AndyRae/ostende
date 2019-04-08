from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import Programme, Venue, Film, Season, Screening, Article

admin.site.register(Programme)
admin.site.register(Venue)
admin.site.register(Film)
admin.site.register(Season)
admin.site.register(Article)


class ScreeningResource(resources.ModelResource):

    class Meta:
        film = fields.Field(
            column_name='film',
            attribute='film',
            widget=ForeignKeyWidget(Film, 'name'))
        model = Screening
        fields = ('id', 'name', 'date', 'start_time', 'tickets', 'film',
                  'venue', 'season', 'programme', 'subtitle', 'q_and_a',)


class ScreeningAdmin(ImportExportModelAdmin):
    resource_class = ScreeningResource


admin.site.register(Screening, ScreeningAdmin)
