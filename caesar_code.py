class Caesar:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key):
        self._encode = dict()
        self._decode = dict()
        n = len(self.alphabet)
        for i in range(n):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % n]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
            self._decode[encoded] = letter
            self._decode[encoded.upper()] = letter.upper()

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])
    