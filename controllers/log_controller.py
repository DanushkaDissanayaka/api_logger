from fastapi import Depends

from controllers.base_controller import BaseController
from model.common.query_param_model import QueryParamModel
from model.log.log_filter_param_model import LogFilterParamModel
from model.log.log_model import LogModel
from service.impl.log_service import LogService
from service.meta.log_service_meta import LogServiceMeta


class LogController(BaseController):
    _log_service: LogServiceMeta

    def __init__(self, log_service: LogServiceMeta = Depends(LogService)):
        self._log_service = log_service

    def add(self, model: LogModel):
        try:
            return self._log_service.add(model=model)
        except Exception as e:
            return self.ise(e)

    def get_by_id(self, _id: str):
        try:
            return self._log_service.get_by_id(_id=_id)
        except Exception as e:
            return self.ise(e)

    def get_all(self,
                _filters: LogFilterParamModel,
                _query: QueryParamModel):
        try:
            return self._log_service.get_all(_filters=_filters, _query=_query)
        except Exception as e:
            return self.ise(e)
