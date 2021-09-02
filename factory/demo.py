from pyfactory.serializers import Serializer

"""
    Object Factory Demonstration
"""
from pyfactory.song import Song
from pyfactory.serializer import ObjectSerializer, Format

song = Song(1, "Water Of Love", "Dire Straits")
serializer = ObjectSerializer()

json_format = serializer.serialize(song, Format.JSON)
yaml_format = serializer.serialize(song, Format.YAML)
xml_format = serializer.serialize(song, Format.XML)

print(json_format)
print(yaml_format)
print(xml_format)
