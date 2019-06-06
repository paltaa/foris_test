import argparse
from functions import dict_list_to_presence_minutes_report, file_to_dict
from pprint import pprint

parser = argparse.ArgumentParser(
    description="Alumni presence report generation tool, code test for Foris.ai")

parser.add_argument('-sp', '--student_presence', type=str,
                    help='.txt file to parse, default is input.txt',
                    default='input.txt')

args = parser.parse_args()
file = args.student_presence
students_presence_dict = file_to_dict(file)
report = dict_list_to_presence_minutes_report(students_presence_dict)
print(report)

students = file_to_dict('nohay.txt')
