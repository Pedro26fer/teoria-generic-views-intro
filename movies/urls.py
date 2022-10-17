from django.urls import path
from .views import ListMoviesView, RetrieveMovieView

urlpatterns = [
    path('movies/', ListMoviesView.as_view()),
    path('movies/<int:pk>/', RetrieveMovieView.as_view()),
]