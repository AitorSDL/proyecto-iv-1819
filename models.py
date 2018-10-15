from django.db.models import Model, UUIDField, CharField,DateTimeField
class Clothes(Model):
    id = UUIDField(primary_key=True)
    name = CharField(max_length=45)
    type = CharField(max_length=45)
    price = CharField(max_length=45)
