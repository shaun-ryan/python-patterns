from .serializers import Serializer


class Song:
    

    def __init__(self, song_id:int, title:str, artist:str):

        self.song_id = song_id
        self.title = title
        self.artist = artist


    def serialize(self, serializer:Serializer):

        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)