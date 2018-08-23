from django.views.generic import ListView
from core.models import Movie
from django.views.generic import(
    ListView, DetailView,
)

class MovieList(ListView):
    model = Movie

class MovieDetail(DetailView):
    model = Movie