from typing import Dict

from pydantic import BaseModel, Extra, constr, StrictStr

NonEmptyStr = constr(strict=True, min_length=1)


class RequestOptionsModel(BaseModel):
    http_headers: Dict[NonEmptyStr, StrictStr] = {}

    class Config:
        extra = Extra.forbid


class RequestOptions(BaseModel):
    request_options: RequestOptionsModel = {}
