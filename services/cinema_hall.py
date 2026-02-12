from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    """
    Retorna todas as salas de cinema.

    :return: QuerySet de todas as salas de cinema
    """
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str,
    hall_rows: int,
    hall_seats_in_row: int,
) -> CinemaHall:
    """
    Cria uma nova sala de cinema.

    :param hall_name: Nome da sala de cinema
    :param hall_rows: Número de fileiras
    :param hall_seats_in_row: Número de assentos por fileira
    :return: Objeto CinemaHall criado
    """
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row,
    )
