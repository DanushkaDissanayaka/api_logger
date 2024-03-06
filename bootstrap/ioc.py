import punq
from service import LogService, LogServiceMeta
from database.repository import LogRepository, LogRepositoryMeta


def get_container() -> punq.Container:
    container = punq.Container()

    # service registration
    container.register(LogServiceMeta, LogService)

    # repository registration
    container.register(LogRepositoryMeta, LogRepository)

    # helper registration

    return container
