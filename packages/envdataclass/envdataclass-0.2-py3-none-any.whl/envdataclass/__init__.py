import dataclasses
import distutils.util
import os
from io import StringIO
from typing import List

from dotenv import dotenv_values


def from_string(schema: dataclasses.dataclass, env_str: str) -> dataclasses.dataclass:
    env_values = dotenv_values(stream=StringIO(env_str))
    return parse_dataclass(schema, env_values)


def from_file(schema: dataclasses.dataclass, env_path: str) -> dataclasses.dataclass():
    if not os.path.exists(env_path):
        raise FileNotFoundError(f'.env file does not exist at provided path ({env_path})')
    env_values = dotenv_values(dotenv_path=env_path)
    return parse_dataclass(schema, env_values)


def parse_dataclass(validator: dataclasses.dataclass, env_values: dict) -> dataclasses.dataclass:
    export = {}
    for a, b in vars(validator).items():
        if a == '__dataclass_fields__':
            for key in b:
                field: dataclasses.Field = b[key]
                if field.name in env_values:
                    value: str = env_values[field.name]
                    try:
                        if field.type is bool:
                            export[field.name] = bool(distutils.util.strtobool(value))
                        elif field.type is int:
                            export[field.name] = int(value)
                        elif field.type is List[int]:
                            export[field.name] = [int(k) for k in value.split(',')]
                        else:
                            export[field.name] = value
                    except ValueError:
                        pass
    return validator(**export)
