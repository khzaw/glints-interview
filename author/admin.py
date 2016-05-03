from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_image')

    def show_image(self, obj):
        if obj.image:
            return u'<img src="%s" height="60" width="60">' % (obj.image)
        return ''
    show_image.short_description = 'Thumbnail'
    show_image.allow_tags = True