from caesar_code import Caesar
import unittest

class TestCaesarCose(unittest.TestCase):
	
	def test_encode_simple(self):
		cipher = Caesar(3)
		result = cipher.encode("абв")
		self.assertEqual(result, "где")
	
	def test_decode_simple(self):
		cipher = Caesar(3)
		encoded = cipher.encode("абв")
		decoded = cipher.decode(encoded)
		self.assertEqual(decoded, "абв")
	
	def test_encode_with_uppercase(self):
		cipher = Caesar(1)
		result = cipher.encode("АбВ")
		self.assertEqual(result, "БвГ")
	
	def test_decode_with_uppercase(self):
		cipher = Caesar(5)
		text = "Привет"
		encoded = cipher.encode(text)
		decoded = cipher.decode(encoded)
		self.assertEqual(decoded, text)
	
	def test_encode_decode_circular(self):
		cipher = Caesar(33)  # длина алфавита = 33 (с ё)
		text = "яюэь"
		encoded = cipher.encode(text)
		decoded = cipher.decode(encoded)
		self.assertEqual(decoded, text)
	
	def test_key_zero(self):
		cipher = Caesar(0)
		text = "тест"
		self.assertEqual(cipher.encode(text), text)
		self.assertEqual(cipher.decode(text), text)
	
	def test_key_negative(self):
		# Отрицательный ключ эквивалентен положительному: (key % len)
		cipher1 = Caesar(-1)
		cipher2 = Caesar(32)  # 33 - 1
		text = "бвг"
		self.assertEqual(cipher1.encode(text), cipher2.encode(text))
	
	def test_non_alphabet_chars_unchanged(self):
		cipher = Caesar(7)
		text = "Привет, мир! 123."
		encoded = cipher.encode(text)
		decoded = cipher.decode(encoded)
		self.assertEqual(decoded, text)
	
	def test_full_cycle_decode_equals_original(self):
		cipher = Caesar(17)
		original = "Съешь же ещё этих мягких французских булок, да выпей чаю!"
		encoded = cipher.encode(original)
		decoded = cipher.decode(encoded)
		self.assertEqual(decoded, original)
	
	def test_empty_string(self):
		cipher = Caesar(10)
		self.assertEqual(cipher.encode(""), "")
		self.assertEqual(cipher.decode(""), "")
	
	def test_only_non_alphabet_chars(self):
		cipher = Caesar(5)
		text = "!@#$% 12345"
		self.assertEqual(cipher.encode(text), text)
		self.assertEqual(cipher.decode(text), text)
		
if __name__ == '__main__':
	unittest.main()