SCHEMA = "http://json-schema.org/draft-07/schema#"
DATETIMEPATTERN = "^(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2})([+-]\\d{4})$"

schema_01 = {
    "$schema": SCHEMA,
    "type": "object",
    "properties": {
        "username": {"type": "string", "pattern": "^[a-z][a-z0-9_]{2,99}$"},
        "password": {
            "type": "string",
            "pattern": "^(?=.*[a-zA-Z])(?=.*\\d).{6,}$",
        },
    },
    "required": ["username", "password"],
    "additionalProperties": False,
}

schema_02 = {
    "$schema": SCHEMA,
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "registeredAt": {"type": "string", "pattern": DATETIMEPATTERN},
        "tokenValidityPeriod": {"type": "integer"},
    },
    "required": [
        "id",
        "username",
        "registeredAt",
        "tokenValidityPeriod",
    ],
}

schema_03 = {
    "$schema": SCHEMA,
    "type": "object",
    "properties": {
        "username": {"type": "string", "pattern": "^[a-z][a-z0-9_]{2,99}$"},
        "password": {
            "type": "string",
            "pattern": "^(?=.*[a-zA-Z])(?=.*\\d).{6,}$",
        },
        "grantType": {"enum": ["password"]},
    },
    "required": ["username", "password", "grantType"],
    "additionalProperties": False,
}
schema_04 = {
    "$schema": SCHEMA,
    "type": "object",
    "properties": {
        "accessToken": {"type": "string"},
        "tokenType": {"type": "string", "enum": ["Bearer"]},
    },
    "required": ["accessToken", "tokenType"],
    "additionalProperties": False,
}