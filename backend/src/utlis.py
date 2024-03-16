from datetime import datetime, timezone
from typing import Any

from flask import jsonify
from jsonschema import validate
from jsonschema.exceptions import SchemaError, ValidationError


def abort(
    message: str = "error occured.",
    code: int = 400,
    target: str = "unknown",
):
    return (
        jsonify(dict(error=dict(message=message, code=code, target=target))),
        code,
    )


def validator(data: Any, schema: dict[str, Any]) -> str | None:
    try:
        validate(data, schema)
    except SchemaError as e:
        return e.message
    except ValidationError as e:
        return e.message
    else:
        return None


def deserialize_datetime(date_string: str) -> datetime:
    given_time = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z")
    utc_time = given_time.astimezone(timezone.utc)
    return utc_time


def serialize_datetime(date_object: datetime) -> str:
    return date_object.strftime("%Y-%m-%dT%H:%M:%S") + "+0000"
