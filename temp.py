from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, Query

app = FastAPI()

_db = {}  # this is a fake implementation of database class


class FilterParams:
    def __init__(self, _date: Annotated[datetime, Query(title="Date time filter")]):
        self.date = _date


class QueryParams:
    def __init__(self,
                 _skip: Annotated[int, Query(title="skip record limit")],
                 _limit: Annotated[int, Query(title="Limit of records to take from database")], ):
        self.skip = _skip
        self.limit = _limit


@app.get("/logs/all")
async def get_all(_filters: Annotated[FilterParams, Depends(FilterParams)],
                  _query: Annotated[QueryParams, Depends(QueryParams)]):
    response = {}
    items = _db.get_logs(limit=_query.limit, skip=_query.skip, filter_date=_filters.date)
    response.update({"data": items})
    return response
