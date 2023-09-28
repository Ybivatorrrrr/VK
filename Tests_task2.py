import unittest
from Task2 import find_matching_lines
import os


class TestFindMatchingLines(unittest.TestCase):
    def test_matching_lines(self):
        with open('test_file.txt', 'w', encoding='utf-8') as file:
            file.write("а Роза упала на лапу Азора\n")
            file.write("Это тестовая строка\n")
            file.write("Другая строка с Розой\n")

        search_words = ['роза', 'Азора']

        expected_lines = ["а Роза упала на лапу Азора", "Другая строка с Розой"]
        result = list(find_matching_lines('test_file.txt', search_words))
        self.assertEqual(result, expected_lines)
        os.remove('test_file.txt')

    def test_no_matching_lines(self):
        with open('test_file.txt', 'w', encoding='utf-8') as file:
            file.write("Это тестовая строка без совпадений\n")
            file.write("Еще одна строка без совпадений\n")

        search_words = ['роза', 'Азора']

        result = list(find_matching_lines('test_file.txt', search_words))
        self.assertEqual(result, [])
        os.remove('test_file.txt')


if __name__ == '__main__':
    unittest.main()
