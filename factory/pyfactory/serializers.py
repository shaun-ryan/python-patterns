import xml.etree.ElementTree as et
import yaml
import json
from abc import ABC, abstractmethod


class Serializer(ABC):

    @abstractmethod
    def start_object(self, object_name:str, object_id):
        pass

    @abstractmethod
    def add_property(self, name:str, value):
        pass

    @abstractmethod
    def to_str(self):
        pass


class JsonSerializer(Serializer):

    def __init__(self):

        self._current_object = None

    def start_object(self, object_name:str, object_id):

        self._current_object = {
            'id': object_id
        }

    def add_property(self, name:str, value):

        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer(Serializer):

    def __init__(self):

        self._element = None

    def start_object(self, object_name:str, object_id):

        self._element = et.Element(object_name, attrib={"id": str(object_id)})

    def add_property(self, name:str, value):

        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding="unicode")


class YamlSerializer(JsonSerializer):

    def to_str(self):
        return yaml.dump(self._current_object)

