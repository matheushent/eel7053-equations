"""Core module for HTTP response operations"""
from typing import Any, Dict

import fastapi
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


def bad_request(body: Dict[str, Any]):

    return JSONResponse(
        content=jsonable_encoder(body),
        status_code=fastapi.status.HTTP_400_BAD_REQUEST,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


def success(body):

    return JSONResponse(
        content=jsonable_encoder(body),
        status_code=fastapi.status.HTTP_200_OK,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


def unauthorized(body):

    return JSONResponse(
        content=jsonable_encoder(body),
        status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


def too_many_requests(body):

    return JSONResponse(
        content=body,
        status_code=fastapi.status.HTTP_429_TOO_MANY_REQUESTS,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


def conflict(body):

    return JSONResponse(
        content=body,
        status_code=fastapi.status.HTTP_409_CONFLICT,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


def unsupported_media_type(body):

    return JSONResponse(
        content=body,
        status_code=fastapi.status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


def created(body):

    return JSONResponse(
        content=body,
        status_code=fastapi.status.HTTP_201_CREATED,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


def not_found(body):

    return JSONResponse(
        content=body,
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        headers={
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    )


class OK(BaseModel):
    """
    A response that there was no error, when no other data is required
    """

    status: str = "ok"
    message: str = ""
