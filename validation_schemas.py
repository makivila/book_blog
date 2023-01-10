from marshmallow import Schema, fields, validate


class BookValidationSchema(Schema):
    author = fields.String(required=True, validate=validate.Length(min=1))
    genre = fields.String(required=True, validate=validate.Length(min=1))
    grade = fields.Integer(validate=validate.Range(min=0, max=10))
    is_finished = fields.Integer(required=True, validate=validate.OneOf([0, 1]))
    opinion = fields.String()
    title = fields.String(required=True, validate=validate.Length(min=1))

class ValidationResult:
    def __init__(self, status, error_messages=None):
        self.status = status
        self.error_messages = error_messages
