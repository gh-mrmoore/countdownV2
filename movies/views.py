from django.shortcuts import render
from .models import MovieCountDown
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
import json

# Create your views here.
def index(request):
    # movies = MovieCountDown.objects.all()
    # movies_serialized = serializers.serialize('json', movies)
    get_movies = MovieCountDown.objects.all()

    # return HttpResponse(movies_serialized, content_type="text/json-comment-filtered")
    context = {'movies': get_movies}
    return render(request, 'movies/index.html', context)

def response(request):
    # get all database objects
    api_response = MovieCountDown.objects.all()

    # create blank lists to add object data
    movie_titles = []
    movie_dates = []

    for movies in api_response:
        movie_titles.append(movies.movieTitle)
        movie_dates.append(movies.movieDate)
    
    return JsonResponse({'movies': movie_titles, 'dates': movie_dates})

def response2(request):
    all_movies = MovieCountDown.objects.all()

    # create blank list to add dictionaries to
    movies_list = []

    for movies in all_movies:
        movie_dict = {'title': movies.movieTitle, 'date': movies.movieDate}
        movies_list.append(movie_dict)
    
    return JsonResponse(movies_list, safe=False)