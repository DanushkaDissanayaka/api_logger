from abc import abstractmethod
from typing import List

from model.common.query_param_model import QueryParamModel
from model.log.log_filter_param_model import LogFilterParamModel
from model.log.log_model import LogModel
from model.log.log_view_model import LogViewModel


class LogServiceMeta:
    @abstractmethod
    def add(self, model: LogModel) -> LogViewModel:
        pass

    @abstractmethod
    def get_by_id(self, _id: str) -> LogViewModel:
        pass

    @abstractmethod
    def edit(self, model: LogModel, _id: str) -> LogViewModel:
        pass

    @abstractmethod
    def get_all(self, _filters: LogFilterParamModel,
                _query: QueryParamModel) -> List[LogViewModel]:
        pass

