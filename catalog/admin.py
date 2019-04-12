from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book,Language


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('last_name',
                    'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]




