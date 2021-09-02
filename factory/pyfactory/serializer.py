from abc import ABC, abstractmethod
from enum import Enum
from .serializers import (
    Serializer, 
    JsonSerializer, 
    XmlSerializer, 
    YamlSerializer
)

class Format(Enum):
    JSON = 1,
    YAML = 2,
    XML = 3


class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format: Format, creator: type):
        self._creators[format] = creator

    def get_serializer(self, format: Format):

        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)

        return creator()


factory = SerializerFactory()
factory.register_format(Format.JSON, JsonSerializer)
factory.register_format(Format.YAML, YamlSerializer)
factory.register_format(Format.XML, XmlSerializer)


class ObjectSerializer:

    def serialize(self, serializable: type, format: Format):

        serializer: Serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()
