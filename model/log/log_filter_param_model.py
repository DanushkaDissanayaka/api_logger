from datetime import datetime
from typing import Annotated

from fastapi import Query


class LogFilterParamModel:
    def __init__(self, _date: Annotated[datetime, Query(title="Date time filter")]):
        self.date = _date
