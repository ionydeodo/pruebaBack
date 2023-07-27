from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from drf_spectacular.types import OpenApiTypes
from django.contrib.auth.models import User



from .serializers import MovieSerializer
from .models.movie import Movie, MovieScore

#1.a ####################################################################################################################################################
@extend_schema(responses={200: MovieSerializer(many=False)})
@api_view(['GET'])
def get_random_series_movie(self):
    movie = Movie.objects.order_by('?').first()
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
#########################################################################################################################################################

#1.b ####################################################################################################################################################
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='order_by',
            location=OpenApiParameter.QUERY,
            type=OpenApiTypes.STR,
            description='name, genre, type, views, score'
        )
    ],
    responses={200: MovieSerializer(many=True)})
@api_view(['GET'])
def get_all_movies_series_series_ordered(request):
    order_by = request.query_params.get('order_by')
    if order_by == 'views' or order_by == 'score' :
        movies = Movie.objects.all().order_by(order_by).reverse()
    else :
        movies = Movie.objects.all().order_by(order_by)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

#########################################################################################################################################################

#1.c ####################################################################################################################################################
@extend_schema(
    parameters=[OpenApiParameter(name='name', location=OpenApiParameter.QUERY, type=OpenApiTypes.STR)],
    responses={200: MovieSerializer(many=True)})
@api_view(['GET'])
def get_series_movies_by_name(request):
    name = request.query_params.get('name', '')
    movies = Movie.objects.filter(name__exact=name)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@extend_schema(
    parameters=[OpenApiParameter(name='genre', location=OpenApiParameter.QUERY, type=OpenApiTypes.STR,
                                description='Comedia, Drama, Terror, Aventura, Accion')],
    responses={200: MovieSerializer(many=True)})
@api_view(['GET'])
def get_movies_series_by_genre(request):
    genre = request.query_params.get('genre', '')
    movies = Movie.objects.filter(genre__exact=genre)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@extend_schema(
    parameters=[OpenApiParameter(name='type', location=OpenApiParameter.QUERY, type=OpenApiTypes.STR,
                                 description='Pelicula, Serie')],
    responses={200: MovieSerializer(many=True)})
@api_view(['GET'])
def get_series_movies_by_type(request):
    type = request.query_params.get('type', '')
    movies = Movie.objects.filter(type__exact=type)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

#########################################################################################################################################################

#1.d ####################################################################################################################################################
@extend_schema(
    parameters=[OpenApiParameter(name='movie_id', location=OpenApiParameter.QUERY, type=OpenApiTypes.INT)])
@api_view(['POST'])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def mark_movie_series_view(request):
    try:
        movie_id = int(request.query_params.get('movie_id', ''))
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({'error': 'The film or series does not exist.'}, status=404)

    if request.user in movie.viewed_users.all():
        return Response({'error': 'You already marked this movie or series as watched.'}, status=400)

    movie.viewed_users.add(request.user)
    movie. views += 1
    movie.save()

    return Response({'message': 'Movie or series marked as successfully viewed.'}, status=200)

#########################################################################################################################################################

#1.e ####################################################################################################################################################
@extend_schema(
    parameters=[OpenApiParameter(name='movie_id', location=OpenApiParameter.QUERY, type=OpenApiTypes.INT),
                OpenApiParameter(name='score', location=OpenApiParameter.QUERY, type=OpenApiTypes.INT, description='1 to 5')])
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def rate_movie_series(request):
    try:
        movie_id = int(request.query_params.get('movie_id', ''))
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({'error': 'The film or series does not exist.'}, status=404)

    if MovieScore.objects.filter(movie=movie, user=request.user).exists():
        return Response({'error': 'You have already rated this movie or series.'}, status=400)

    score = int(request.query_params.get('score', None))
    if not score or not 1 <= score <= 5:
        return Response({'error': 'The score must be a number between 1 and 5.'}, status=400)

    user_instance = User.objects.get(id=request.user.id)
    movie.users_scored.add(user_instance, through_defaults={'score': score})

    total_scores = movie.users_scored.count()
    current_total_score = movie.score * (total_scores - 1)
    new_total_score = current_total_score + score
    movie.score = new_total_score / total_scores
    
    movie.save()

    return Response({'message': 'Successfully scored film or series.'}, status=200)
#########################################################################################################################################################

#########################################################################################################################################################
class MyTokenObtainPairView(TokenObtainPairView):
    pass

class MyTokenRefreshView(TokenRefreshView):
    pass
#########################################################################################################################################################
