from django.contrib import admin
from .models import Book, Tag


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'price', 'rating', 'show_image', 'show_tags')

    def author_name(self, obj):
        return obj.author.name
    author_name.short_description = 'Author'
    author_name.allow_tags = True

    def show_tags(self, obj):
        if obj.tags.count() >=1 :
            return ','.join(x.name for x in obj.tags.all())
        return ''
    show_tags.short_description = 'Tags'
    show_tags.allow_tags = True

    def show_image(self, obj):
        if obj.url:
            return u'<img src="%s" height="50" width="50">' % obj.url
        return ''
    show_image.short_description = 'Image'
    show_image.allow_tags = True


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
