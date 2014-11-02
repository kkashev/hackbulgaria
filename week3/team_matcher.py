import requests


def get_data():
    data = requests.get("https://hackbulgaria.com/api/students/", verify=False)
    json_file = data.json()
    return json_file


def is_ok():
        if get_data() == 200:
            return True


def list_courses(json_file):
    list_courses = []
    for student in json_file:
        for course in student['courses']:
            if course['name'] not in list_courses:
                list_courses.append(course['name'])
    return(list_courses)


def list_names(json_file):
    list_names = []
    for student in json_file:
        if student['name'] not in list_names:
            list_names.append(student['name'])
    print(list_names)


def print_courses(list_courses):
    for course in list_courses:
        print(course)


def match_command(json_file, course_id, team_size, group_time):
    course_list = []
    for student in json_file:
        


def main():
    json_file = get_data()
    a = list_courses(json_file)
    print_courses(a)
    list_names(json_file)

if __name__ == '__main__':
    main()
