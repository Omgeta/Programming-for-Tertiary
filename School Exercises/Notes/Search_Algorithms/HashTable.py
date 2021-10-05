class HashTable:
    """ HashTable implementation for storing key-value pairs """

    def __init__(self, size: int = 32):
        """ Constructs a static array of specified size to hold elements """
        self.size = size
        self.data = [None] * self.size

    def __hash(self, key: str) -> int:
        """ Hash function for the table """
        # any hash function will do
        hash_str = hash(key) % self.size
        return hash_str

    def set(self, key: str, value: any):
        """ Sets value to the specified key in the HashTable """
        hash_str = self.__hash(key)
        self.data[hash_str] = value

    def get(self, key: str) -> any:
        """ Gets value from the key in the HashTable """
        hash_str = self.__hash(key)
        return self.data[hash_str]
