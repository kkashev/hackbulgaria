import unittest
from counting_words import count_words


class TestCountingWords(unittest.TestCase):

    def test_count_words(self):
        input = count_words(["apple", "banana", "apple", "pie"])
        output = {'apple': 2, 'pie': 1, 'banana': 1}
        self.assertEquals(output, input)

if __name__ == '__main__':
    unittest.main()
