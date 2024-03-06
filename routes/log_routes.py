from fastapi import APIRouter, Depends

from controllers import LogController
from model.log.log_model import LogModel

loger_router = APIRouter(prefix='/log', tags=['Log'])


@loger_router.get("{_id}")
async def get_log(_id: str, controller: LogController = Depends(LogController)):
    return controller.get_by_id(_id=_id)


@loger_router.post("")
async def create_log(model: LogModel, controller: LogController = Depends(LogController)):
    return controller.add(model)
