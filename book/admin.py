from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'price', 'rating', 'show_image')

    def author_name(self, obj):
        return obj.author.name
    author_name.short_description = 'Author'
    author_name.allow_tags = True

    def show_image(self, obj):
        if obj.url:
            return u'<img src="%s" height="50" width="50">' % obj.url
        return ''
    show_image.short_description = 'Image'
    show_image.allow_tags = True