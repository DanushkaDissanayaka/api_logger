from typing import List

from database.repository.meta.log_repository_meta import LogRepositoryMeta
from model.common.query_param_model import QueryParamModel
from model.log.log_filter_param_model import LogFilterParamModel
from model.log.log_model import LogModel
from model.log.log_view_model import LogViewModel


class LogRepository(LogRepositoryMeta):

    def add(self, model: LogModel) -> LogViewModel:
        # map log model to data class
        # log to storage implementation
        return LogViewModel('Log created')

    def get_by_id(self, _id: str) -> LogViewModel:
        # Getting log from storage implementation

        return LogViewModel('Log get by id')

    def edit(self, model: LogModel, _id: str) -> LogViewModel:
        # map log model to dataclass
        # Edit log implementation
        return LogViewModel('Log has edited')

    def get_all(self,
                _filters: LogFilterParamModel,
                _query: QueryParamModel
                ) -> List[LogViewModel]:
        # Implementation get all log record from storage
        return [LogViewModel('Log record 1'),
                LogViewModel('Log record 2'),
                LogViewModel('Log record 3')]
