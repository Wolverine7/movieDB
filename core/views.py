from django.views.generic import ListView
from core.models import Movie
from django.views.generic import(
    ListView, DetailView,
)

class MovieList(ListView):
    model = Movie

class MovieDetail(DetailView):
    queryset = (
        Movie.objects.all_with_related_persons()
    )