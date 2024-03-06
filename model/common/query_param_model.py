from typing import Annotated

from fastapi import Query


class QueryParamModel:
    def __init__(self,
                 _skip: Annotated[int, Query(title="skip record limit")],
                 _limit: Annotated[int, Query(title="Limit of records to take from database")], ):
        self.skip = _skip
        self.limit = _limit
