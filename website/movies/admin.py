from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from movies.models import Movie


class MovieAdmin(ModelAdmin):
    model = Movie
    menu_label = 'Movies'
    menu_icon = 'fa-film'
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title', 'year', 'director', 'genre')
    search_fields = ('title', 'release_date__year', 'director', 'genre')


modeladmin_register(MovieAdmin)
