from bootstrap import IOCService
from model.log.log_model import LogModel
from service.meta.log_service_meta import LogServiceMeta


class LogController:
    _log_service: LogServiceMeta

    def __init__(self, log_service: LogServiceMeta = IOCService(LogServiceMeta)):
        self._log_service = log_service

    def add(self, model: LogModel):
        return self._log_service.add(model=model)

    def get_by_id(self, _id: str):
        return self._log_service.get_by_id(_id=_id)
