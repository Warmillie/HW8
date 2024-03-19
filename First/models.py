from mongoengine import Document, EmbeddedDocument, StringField, ListField, ReferenceField, connect


connect(host='mongodb+srv://warmillie1:%23EDCxsw2!QAZ@cluster0.ezi9yvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

class Quote(Document):
    text = StringField(required=True)
    author = StringField(required=True)
    tags = ListField(StringField())