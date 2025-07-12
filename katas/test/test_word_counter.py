import unittest
from katas.word_count import count_words


class Test_word_counter(unittest.TestCase):
    def test_count_words(self):
        sentence = "This is a sample sentence for counting words."
        word_count = count_words(sentence)
        self.assertEqual(word_count, 8)
        self.assertIsInstance(word_count, int)
    def test_count_words_empty_str(self):
        sentence = ""
        word_count = count_words(sentence)
        self.assertEqual(word_count, 0)
        self.assertIsInstance(word_count, int)
    def test_count_words_spaces_only(self):
        sentence = "   "
        word_count = count_words(sentence)
        self.assertEqual(word_count, 0)
        self.assertIsInstance(word_count, int)
        
