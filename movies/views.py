from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Movie
from .serializers import MovieSerializer


# class ListMoviesView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serialized_movies = MovieSerializer(movies, many=True)

#         return Response(serialized_movies.data)

class ListMoviesView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# class RetrieveMovieView(APIView):
#     def get(self, request, pk=''):
#         movie = get_object_or_404(Movie, pk=pk)
#         serialized_movie = MovieSerializer(movie)
        
#         return Response(serialized_movie.data)


class RetrieveMovieView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


    