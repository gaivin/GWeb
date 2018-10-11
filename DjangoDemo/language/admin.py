from django.contrib import admin
from language.models import Language, Rating


# Register your models here.


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'language_type')
    search_fields = ('language_type',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('language', 'sample_date', 'rating')
    search_fields = ('language',)


admin.site.register(Language, LanguageAdmin)
admin.site.register(Rating, RatingAdmin)
