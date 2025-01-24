from django.contrib import admin
from .models import Lux_precious_metal

from seshat.apps.core.models import Prec_met_instance

admin.site.register(Prec_met_instance)

class Lux_preciousMetalAdmin(admin.ModelAdmin):
    exclude = ('citations', 'comment', 'private_comment')  # Exclude fields from the form

admin.site.register(Lux_precious_metal, Lux_preciousMetalAdmin)