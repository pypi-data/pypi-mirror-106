from typing import Tuple
from fastapi.responses import JSONResponse
from .dataclases import ErrorResponse, Error


def error_types_responses(*codes: Tuple):
    return { k: { "model": ErrorResponse } for k in codes }

def get_error_response(text: str):
    return ErrorResponse(error=Error(text=text)).dict()

def JSONErrorResponse(status_code: int, text: str):
    return JSONResponse(status_code=status_code, content=get_error_response(text=text))