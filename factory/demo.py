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

"""
    Generic Factory Demonstration
"""

# The config dictionary contains all the values required to initialize each of the services.

from pyfactory_generic import music

config = {
    'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
    'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
    'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
    'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET',
    'local_music_location': '/usr/data/music'
}

pandora = music.services.get('PANDORA', **config)
pandora.test_connection()

spotify = music.services.get('SPOTIFY', **config)
spotify.test_connection()

local = music.services.get('LOCAL', **config)
local.test_connection()

pandora2 = music.services.get('PANDORA', **config)
print(f'id(pandora) == id(pandora2): {id(pandora) == id(pandora2)}')

spotify2 = music.services.get('SPOTIFY', **config)
print(f'id(spotify) == id(spotify2): {id(spotify) == id(spotify2)}')