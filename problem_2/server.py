from flask import Flask
from marshmallow import Schema, fields

app = Flask(__name__)


class AccountSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)


class SampleSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    active = fields.Boolean(required=True)
    count = fields.Integer(required=True)
    address_ids = fields.List(fields.Integer(), required=True)
    accounts = fields.Nested(AccountSchema, required=True, many=True)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
