from flask import request as flask_request
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from functools import wraps


class InputValidator(Inputs):
    def __new__(cls, schema, *args, **kwargs):
        cls.json = [JsonSchema(schema=schema)]
        return super(InputValidator, cls).__new__(cls)

    def __init__(self, request, *args, **kwargs):
        super(InputValidator, self).__init__(request)


def validate_input(schema, response):
    def decorator(f):
        @wraps(f)
        def func_wrapper(*args, **kwargs):
            input_validity = InputValidator(request=flask_request, schema=schema)
            if not input_validity.validate():
                if callable(response):
                    return response(input_validity.errors)
                return response
            return f(*args, **kwargs)

        return func_wrapper

    return decorator
