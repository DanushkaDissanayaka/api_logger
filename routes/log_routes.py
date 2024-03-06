from fastapi import APIRouter, Depends

from controllers import LogController
from model.common.query_param_model import QueryParamModel
from model.log.log_filter_param_model import LogFilterParamModel
from model.log.log_model import LogModel

loger_router = APIRouter(prefix='/log', tags=['Log'])


@loger_router.get("/get/{_id}")
async def get_log(_id: str, controller: LogController = Depends(LogController)):
    return controller.get_by_id(_id=_id)


@loger_router.post("/create")
async def create_log(model: LogModel, controller: LogController = Depends(LogController)):
    return controller.add(model)


@loger_router.post("/get")
async def create_log(_filters: LogFilterParamModel = Depends(LogFilterParamModel),
                     _query: QueryParamModel = Depends(QueryParamModel),
                     controller: LogController = Depends(LogController)):
    return controller.get_all(_filters=_filters, _query=_query)
