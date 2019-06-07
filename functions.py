from datetime import timedelta
import itertools as it


def file_to_dict(file_path):
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        print('File not found')
        return 0
    students_presence_dict = {}
    for line in file:
        line = line.replace('\n', '')
        if 'Student' in line:
            student = line.split(' ')[1]
            students_presence_dict[student] = list()
        elif 'Presence' in line:
            presence_vector = line.split(' ')
            students_presence_dict[presence_vector[1]].append(
                presence_vector[2:])
    file.close()
    return students_presence_dict


def dict_list_to_presence_minutes_report(students_presence_dict):
    report_list = list()
    for key, presence_list in students_presence_dict.items():
        total_minutes = timedelta(minutes=0)
        days = set()
        for presence in presence_list:
            time_start = presence[1].split(':')
            time_end = presence[2].split(':')
            minutes = timedelta(hours=int(time_end[0]), minutes=int(time_end[1])) - \
                timedelta(hours=int(time_start[0]), minutes=int(time_start[1]))
            days.add(presence[0])
            if minutes > timedelta(minutes=5):
                total_minutes += minutes
        len_days = len(days)
        if len_days == 0:
            days_str = ''
        elif len_days == 1:
            days_str = 'in 1 day'
        else:
            days_str = 'in {} days'.format(len_days)
        alumni_string = '{}: {} minutes {}'.format(key,
                                                   int(total_minutes.seconds/60),
                                                   days_str)
        report_list.append(alumni_string)
        print(alumni_string)
    return report_list


def dict_list_to_student_movement_report(students_presence_dict):
    report_list = list()
    for key, presence_list in students_presence_dict.items():
        day_strings = list()
        for day, group in it.groupby(presence_list, key=get_presence_day):
                #print(key, day, list(group))
            classrooms = [get_presence_clasroom(presence) for presence in group]
            day_strings.append((' -> ').join(classrooms))
        print('{}: {}'.format(key, (',').join(day_strings)))


def get_presence_day(presence):
    return presence[0]


def get_presence_clasroom(presence):
    return presence[3]
