from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Book, Tag
import string


class BookListRedirectView(RedirectView):
    permanent = True
    pattern_name = 'book:list'


class BookListView(ListView):
    model = Book
    paginate_by = 15
    context_object_name = 'books'

    def get_queryset(self):
        get_params = self.request.GET.getlist('tags')
        if get_params:
            return Book.objects.filter(tags__name__in=get_params)
        return super(BookListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        tags = Tag.objects.all().distinct()
        context = super(BookListView, self).get_context_data(**kwargs)
        adjacent_pages = 2
        page_number = context['page_obj'].number
        num_pages = context['paginator'].num_pages
        start_page = max(page_number - adjacent_pages, 1)
        if start_page <= 2:
            start_page = 1
        end_page =  page_number + adjacent_pages + 1
        if end_page >= num_pages + 1:
            end_page = num_pages + 1

        page_numbers = [n for n in xrange(start_page, end_page) \
                        if n > 0 and n <= num_pages]

        filtered_tags = ', '.join(string.capitalize(t) for t in self.request.GET.getlist('tags'))
        context.update({
            'page_numbers': page_numbers,
            'show_first': 1 not in page_numbers,
            'show_last': num_pages not in page_numbers,
            'tags': tags,
            'filtered_tags': filtered_tags
        })
        return context


class BookDetailView(DetailView):
    model = Book

