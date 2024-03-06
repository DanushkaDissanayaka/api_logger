from typing import List

from fastapi import Depends

from database.repository.impl.log_repository import LogRepository
from database.repository.meta.log_repository_meta import LogRepositoryMeta
from model.common.query_param_model import QueryParamModel
from model.log.log_filter_param_model import LogFilterParamModel
from model.log.log_model import LogModel
from model.log.log_view_model import LogViewModel
from service.meta.log_service_meta import LogServiceMeta


class LogService(LogServiceMeta):
    _log_repository: LogRepositoryMeta

    def __init__(self, log_repository: LogRepositoryMeta = Depends(LogRepository)):
        self._log_repository = log_repository

    def add(self, model: LogModel) -> LogViewModel:
        # implementation of business logic to add log records to database

        # add log record to data storage
        return self._log_repository.add(model)

    def get_by_id(self, _id: str) -> LogViewModel:
        # implementation of business logic to retrieve
        # and return log record from data storage

        # retrieve log record from data storage
        return self._log_repository.get_by_id(_id=_id)

    def edit(self, model: LogModel, _id: str) -> LogViewModel:
        # business logic implementation to edit log record in data storage
        # edit and retrieve log record in data storage
        return self._log_repository.edit(model=model, _id=_id)

    def get_all(self, _filters: LogFilterParamModel,
                _query: QueryParamModel) -> List[LogViewModel]:
        # business logic to fiter and retrieve all record from data storage
        # retrieve all log record from storage
        return self._log_repository.get_all(_filters=_filters, _query=_query)
