import unittest
from io import StringIO
import word_processor
import sys

class MyTestC(unittest.TestCase):

    def test_lowercase(self):

        output = StringIO()
        sys.stdout = output

        words = word_processor.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement', 'times', 'what', 'say', 'you'],words)
    
    def test_longer_than(self):
        
        output = StringIO()
        sys.stdout = output

        words_longer = word_processor.words_longer_than(10,'These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['interesting','understatement'],words_longer)

    def test_word_length(self):

        output = StringIO()
        sys.stdout = output

        word_lengths = word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual({2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1},word_lengths)

    def test_letters_count_map(self):

        output = StringIO()
        sys.stdout = output

        letters_count = word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual({'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 7, 'u': 3, 'v': 1, 'w': 0, 'x': 0, 'y': 2, 'z': 0},letters_count)

    
    def test_most_letter(self):

        output = StringIO()
        sys.stdout = output

        popular_char = word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual("e",popular_char)

if __name__ == "__main__":  
    unittest.main()
