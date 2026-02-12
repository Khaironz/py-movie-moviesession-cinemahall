from datetime import datetime
from typing import Optional

from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int,
) -> MovieSession:
    """
    Cria uma nova sessão de filme.

    :param movie_show_time: Horário de exibição do filme
    :param movie_id: ID do filme
    :param cinema_hall_id: ID da sala de cinema
    :return: Objeto MovieSession criado
    """
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(
        session_date: Optional[str] = None) -> QuerySet[MovieSession]:
    """
    Retorna sessões de filmes, opcionalmente filtradas por data.

    :param session_date: Data no formato "ano-mês-dia" (opcional)
    :return: QuerySet de sessões de filmes
    """
    queryset: QuerySet[MovieSession] = MovieSession.objects.all()

    if session_date is not None:
        # Converte a string de data para objeto datetime
        date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        queryset = queryset.filter(show_time__date=date_obj)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    """
    Retorna uma sessão de filme pelo ID.

    :param movie_session_id: ID da sessão de filme
    :return: Objeto MovieSession
    """
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: Optional[datetime] = None,
    movie_id: Optional[int] = None,
    cinema_hall_id: Optional[int] = None,
) -> MovieSession:
    """
    Atualiza uma sessão de filme com os campos fornecidos.

    :param session_id: ID da sessão de filme
    :param show_time: Novo horário de exibição (opcional)
    :param movie_id: Novo ID do filme (opcional)
    :param cinema_hall_id: Novo ID da sala de cinema (opcional)
    :return: Objeto MovieSession atualizado
    """
    movie_session: MovieSession = MovieSession.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = show_time

    if movie_id is not None:
        movie_session.movie_id = movie_id

    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    """
    Deleta uma sessão de filme pelo ID.

    :param session_id: ID da sessão de filme
    """
    movie_session: MovieSession = MovieSession.objects.get(id=session_id)
    movie_session.delete()
