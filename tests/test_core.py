# test_core.py
import os
import json
import unittest
from excel_reader import read_csv, read_excel

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILES_DIR = os.path.join(THIS_DIR, os.pardir, 'test_files')

class TestReader(unittest.TestCase):
    def test_csv(self):
        csv_file = os.path.join(TEST_FILES_DIR, 'students.csv')
        json_file = os.path.join(TEST_FILES_DIR, 'students.json')
        result = read_csv(csv_file)
        with open(json_file, 'r') as f:
            expected = json.load(f)
        self.assertEqual(result.to_dict(), expected)

    def test_excel(self):
        excel_file = os.path.join(TEST_FILES_DIR, 'school.xlsx')
        json_file = os.path.join(TEST_FILES_DIR, 'school.json')
        result = read_excel(excel_file)
        with open(json_file, 'r') as f:
            expected = json.load(f)
        self.assertEqual(result.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
