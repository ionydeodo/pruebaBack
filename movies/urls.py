from django.urls import path
from . import views


urlpatterns = [
    path('random series or movie/', views.get_random_series_movie),
    path('all movies and series ordered/', views.get_all_movies_series_series_ordered,),
    path('movies and series by by name/', views.get_series_movies_by_name),
    path('movies and series by by type/', views.get_series_movies_by_type),
    path('movies and series by genre/', views.get_movies_series_by_genre),
    path('bookmark movie series view/', views.mark_movie_series_view),
    path('rate movie series/', views.rate_movie_series),
    path('token/', views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', views.MyTokenRefreshView.as_view()),
]