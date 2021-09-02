class ObjectFactory:
    """
    A general purpose Object Factory (ObjectFactory) can leverage 
    the generic Builder interface to create all kinds of objects. 
    It provides a method to register a Builder based on a key
    value and a method to create the concrete object instances
    based on the key
    """

    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)