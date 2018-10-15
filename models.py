from django.db.models import Model, UUIDField, CharField, EmailField, DateTimeField
class Clothe(Model):
    id = UUIDField(primary_key=True)
    name = CharField(max_length=45)
    type = CharField(max_length=45)
