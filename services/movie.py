from typing import Iterable, Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
    genres_ids: Optional[Iterable[int]] = None,
    actors_ids: Optional[Iterable[int]] = None,
) -> QuerySet[Movie]:
    """
    Retorna filmes filtrados por gêneros e/ou atores.

    :param genres_ids: Lista de IDs de gêneros (opcional)
    :param actors_ids: Lista de IDs de atores (opcional)
    :return: QuerySet de filmes
    """
    queryset: QuerySet[Movie] = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    """
    Retorna um filme pelo ID.

    :param movie_id: ID do filme
    :return: Objeto Movie
    """
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[Iterable[int]] = None,
    actors_ids: Optional[Iterable[int]] = None,
) -> Movie:
    """
    Cria um novo filme com título, descrição, gêneros e atores.

    :param movie_title: Título do filme
    :param movie_description: Descrição do filme
    :param genres_ids: Lista de IDs de gêneros (opcional)
    :param actors_ids: Lista de IDs de atores (opcional)
    :return: Objeto Movie criado
    """
    movie: Movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids is not None:
        movie.genres.set(genres_ids)

    if actors_ids is not None:
        movie.actors.set(actors_ids)

    return movie
