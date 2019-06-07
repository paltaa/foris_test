import argparse
from functions import dict_list_to_presence_minutes_report, file_to_dict, dict_list_to_student_movement_report
from pprint import pprint

parser = argparse.ArgumentParser(
    description="Alumni presence report generation tool, code test for Foris.ai")

parser.add_argument('-sp', '--student_presence', type=str,
                    help='.txt file to parse, default is input.txt',
                    default='input.txt')

args = parser.parse_args()
file = args.student_presence
students_presence_dict = file_to_dict(file)
pprint(students_presence_dict)
report = dict_list_to_presence_minutes_report(students_presence_dict)
print(report)

dict_list_to_student_movement_report(students_presence_dict)
