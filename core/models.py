from mongoengine import (
    fields,
    DynamicDocument,
)


class Post(DynamicDocument):
    title = fields.StringField()
    body = fields.StringField()
    status = fields.StringField()
    author = fields.StringField()
    tag = fields.ListField()
