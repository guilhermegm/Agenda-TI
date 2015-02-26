
from schematics.types import StringType, BooleanType, DateType
from schematics.types.compound import ListType, ModelType
from mingus.service.models import BaseModel

class Eventos(BaseModel):
    nome = StringType(max_length=100, required=True)
    data = DateType()
    local = StringType(max_length=100)
    endereco = StringType(max_length=100)
    site = StringType(max_length=100)

    class Meta:
        list_allowed_methods = ['get',]