from django.views.generic import ListView
from core.models import Movie
from django.views.generic import(
    ListView, DetailView,
)

class MovieList(ListView):
    model = Movie

    class Meta:
        ordering = ('-year', 'title')

    def __str__(selfs):
        return '{} ({})'.format(
            self.title, self.year
        )

class MovieDetail(DetailView):
    model = Movie