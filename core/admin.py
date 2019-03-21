from django.contrib import admin
from .models import Venue, Film, Season, Screening

admin.site.register(Venue)
admin.site.register(Film)
admin.site.register(Season)
admin.site.register(Screening)
