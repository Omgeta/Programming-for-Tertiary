#Task 1.1
def getIDString(n):
    from string import ascii_letters as alphabet
    from random import randint

    result = ""
    for _ in range(n):
        result += alphabet[randint(0, len(alphabet)-1)]
    return result


#Task 1.2
class HashTable:
    def __init__(self, size):
        self.size = size
        self._data = [None] * self.size

    def _hash(self, string):
        index = 0
        for i, char in enumerate(string, 1):
            index += (ord(char)**2)*i
        return index % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self._data[index] = value

    def get(self, key):
        index = self._hash(key)
        return self._data[index]

    
#Task 1.3
class URLTable(HashTable):
    def insert(self, urlstring):
        while True:
            key = getIDString(8)
            index = self._hash(key)
            if self._data[index] is None:
                self._data[index] = urlstring
                return key

    def list(self):
        for each in self._data:
            print(each)


#Task 1.4
utable = URLTable(3)
for each in ("www.google.com", "www.facebook.com", "www.instagram.com"):
    utable.insert(each)
utable.list()

