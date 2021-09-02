from . import object_factory

class SpotifyService:

    def __init__(self, access_code):
        self._access_code = access_code

    def test_connection(self):
        print(f'Accessing Spotify with {self._access_code}')


class SpotifyServiceBuilder:

    """
    The example shows a SpotifyServiceBuilder that implements 
    .__call__(spotify_client_key, spotify_client_secret, **_ignored).

    This method is used to create and initialize the concrete SpotifyService. 
    It specifies the required parameters and ignores any additional parameters 
    provided through **_ignored. Once the access_code is retrieved, it creates 
    and returns the SpotifyService instance.

    Notice that SpotifyServiceBuilder keeps the service instance around and 
    only creates a new one the first time the service is requested. This 
    avoids going through the authorization process multiple times as specified
    in the requirements.
    """

    def __init__(self):
        self._instance = None

    def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
        if not self._instance:
            access_code = self.authorize(
                spotify_client_key, spotify_client_secret)
            self._instance = SpotifyService(access_code)
        return self._instance

    def authorize(self, key, secret):
        return 'SPOTIFY_ACCESS_CODE'

class PandoraService:

    def __init__(self, consumer_key, consumer_secret):
        self._key = consumer_key
        self._secret = consumer_secret

    def test_connection(self):
        print(f'Accessing Pandora with {self._key} and {self._secret}')


class PandoraServiceBuilder:

    """
    The PandoraServiceBuilder implements the same interface,
    but it uses different parameters and processes to create
    and initialize the PandoraService. It also keeps the
    service instance around, so the authorization only happens once.
    """

    def __init__(self):
        self._instance = None

    def __call__(self, pandora_client_key, pandora_client_secret, **_ignored):
        if not self._instance:
            consumer_key, consumer_secret = self.authorize(
                pandora_client_key, pandora_client_secret)
            self._instance = PandoraService(consumer_key, consumer_secret)
        return self._instance

    def authorize(self, key, secret):
        return 'PANDORA_CONSUMER_KEY', 'PANDORA_CONSUMER_SECRET'


class LocalService:

    def __init__(self, location):
        self._location = location

    def test_connection(self):
        print(f'Accessing Local music at {self._location}')


def create_local_music_service(local_music_location, **_ignored):

    """
    The LocalService just requires a location where the collection
    is stored to initialize the LocalService.

    A new instance is created every time the service is requested
    because there is no slow authorization process. The
    requirements are simpler, so you don’t need a Builder class.
    Instead, a function returning an initialized LocalService is
    used. This function matches the interface of the .__call__()
    methods implemented in the builder classes
    """

    return LocalService(local_music_location)


class MusicServiceProvider(object_factory.ObjectFactory):
    """
    The example above shows that, to access a music service, music.factory.create() 
    is called. This may lead to confusion. Other developers might believe 
    that a new instance is created every time and decide that they should 
    keep around the service instance to avoid the slow initialization process.

    You know that this is not what happens because the Builder class 
    keeps the initialized instance and returns it for subsequent calls, 
    but this isn’t clear from just reading the code.

    A good solution is to specialize a general purpose implementation
    to provide an interface that is concrete to the application context.
    In this section, you will specialize ObjectFactory in the context
    of our music services, so the application code communicates the
    intent better and becomes more readable.

    The following example shows how to specialize ObjectFactory, providing
    an explicit interface to the context of the application:
    """
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


# The music module exposes the ObjectFactory instance through the factory attribute. 
# Then, the builders are registered with the instance. For Spotify and Pandora, 
# you register an instance of their corresponding builder, 
# but for the local service, you just pass the function.
services = MusicServiceProvider()
services.register_builder('SPOTIFY', SpotifyServiceBuilder())
services.register_builder('PANDORA', PandoraServiceBuilder())
services.register_builder('LOCAL', create_local_music_service)




