import unittest
from VigenereCipher import VigenereCipher


class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher("key")

    def test_equalizeKeyword(self):
        message = "HELLOWORLD"
        self.assertEqual(len(self.cipher.equalizeKeyword(message)), len(message))

    def test_encrypt(self):
        self.assertEqual(self.cipher.encrypt("HELLO"), "RIJVS")
        self.assertEqual(self.cipher.encrypt("WORLD"), "GSPVH")

    def test_decrypt(self):
        self.assertEqual(self.cipher.decrypt("RIJVS"), "HELLO")
        self.assertEqual(self.cipher.decrypt("GSPVH"), "WORLD")

    def test_encrypt_with_spaces(self):
        self.assertEqual(self.cipher.encrypt("HELLO WORLD"), "RIJVS GSPVH")

    def test_decrypt_with_spaces(self):
        self.assertEqual(self.cipher.decrypt("RIJVS GSPVH"), "HELLO WORLD")

    def test_special_symbols(self):
        message = "Hello, world!"
        self.assertEqual(self.cipher.encrypt(message), "Rijvs, ambpb!")

    def test_upper_same_as_lower(self):
        message_lower = "hello"
        message_upper = "HELLO"
        self.assertEqual(self.cipher.encrypt(message_upper), self.cipher.encrypt(message_lower).upper())

if __name__ == '__main__':
    unittest.main()
