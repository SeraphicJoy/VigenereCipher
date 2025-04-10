class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def equalizeKeyword(self, message):
        key_length = len(self.key)
        message_length = len(message)
        extended_key = (self.key * (message_length // key_length)) + self.key[:message_length % key_length]
        return extended_key

    def encrypt(self, message):
        extended_key = self.equalizeKeyword(message)
        encrypted_message = []

        for m, k in zip(message, extended_key):
            if m.isalpha():
                key = ord(k) if m.isupper() else ord(k.lower())
                base = ord('A') if m.isupper() else ord('a')
                shift = (ord(m) + key - 2 * base) % 26
                encrypted_message.append(chr(shift + base))
            else:
                encrypted_message.append(m)

        return ''.join(encrypted_message)

    def decrypt(self, encrypted_message):
        extended_key = self.equalizeKeyword(encrypted_message)
        decrypted_message = []

        for e, k in zip(encrypted_message, extended_key):
            if e.isalpha():
                key = ord(k) if e.isupper() else ord(k.lower())
                base = ord('A') if e.isupper() else ord('a')
                shift = (ord(e) - key + 26) % 26
                decrypted_message.append(chr(shift + base))
            else:
                decrypted_message.append(e)

        return ''.join(decrypted_message)

key = "key"
message = "Hello, world!"
print(VigenereCipher(key).encrypt(message), VigenereCipher(key).decrypt(VigenereCipher(key).encrypt(message)), sep='\n')
print(VigenereCipher(key).decrypt(message))