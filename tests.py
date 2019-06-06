import unittest
from functions import dict_list_to_presence_minutes_report, file_to_dict


class FileToDict(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(file_to_dict('empty_file.txt'), {})

    def test_1(self):
        result = {'David': [['5', '14:02', '15:46', 'F505']],
                  'Fran': [],
                  'Marco': [['1', '09:02', '10:17', 'R100'], ['3', '10:58', '12:05', 'R205']]}
        file = 'input.txt'
        self.assertEqual(file_to_dict(file), result)

    def test_file_not_found(self):
        file = 'no_file.txt'
        self.assertEqual(file_to_dict(file), 0)


class MinutesReport(unittest.TestCase):
    def test_empty(self):
        file = 'empty_file.txt'
        students_presence_dict = file_to_dict(file)
        report = dict_list_to_presence_minutes_report(students_presence_dict)
        self.assertEqual(report, [])

    def test_1(self):
        result = ['David: 104 minutes in 1 day',
                  'Marco: 142 minutes in 2 days',
                  'Fran: 0 minutes ']
        file = 'input.txt'
        students_presence_dict = file_to_dict(file)
        report = dict_list_to_presence_minutes_report(students_presence_dict)
        self.assertEqual(set(report), set(result))


if __name__ == '__main__':
    unittest.main()
