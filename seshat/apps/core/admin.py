from django.contrib import admin
from .models import (
    Macro_region,
    Seshat_region,
    Polity,
    Country,
    Section,
    Subsection,
    Citation,
    Reference,
    Variablehierarchy,
    SeshatComment,
    SeshatCommentPart,
    Nga,
    Ngapolityrel,
    Capital,
    Religion,
)

admin.site.register(Macro_region)
admin.site.register(Seshat_region)
admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Variablehierarchy)
admin.site.register(Polity)
admin.site.register(Country)
admin.site.register(Citation)
admin.site.register(Reference)
admin.site.register(SeshatComment)
admin.site.register(SeshatCommentPart)
admin.site.register(Nga)
admin.site.register(Ngapolityrel)
admin.site.register(Capital)
admin.site.register(Religion)


class CustomReferenceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_date",
        "creator",
    )


admin.site.unregister(Reference)
admin.site.register(Reference, CustomReferenceAdmin)
