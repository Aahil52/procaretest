import json
from datetime import datetime


def get_last_sign_out(students_attendance):
    sign_out_times = []
    for i in range(len(students_attendance)):
        sot_str = students_attendance[i]['sign_out_time']
        sot_obj = datetime.strptime(sot_str, '%Y-%m-%d %H:%M')
        sign_out_times.append((students_attendance[i]['student_id'], sot_obj))
    sign_out_times.sort(key=lambda x: x[1], reverse = True)
    return sign_out_times[0][0]

def get_room_name(rooms, id):
    for i in range(len(rooms)):
        if rooms[i]['id'] == id:
            return rooms[i]['name']

# Would be call to Students Attendance with school_id as parameter
sa = open('students_attendance.json')
students_attendance = json.load(sa)['attendance']

student_id = get_last_sign_out(students_attendance)
print(student_id)

# Would be call to Student Detailed Info with student_id and school_id as parameter
sdi = open('student_detailed_info/' + student_id + '.json')
student_detailed_info = json.load(sdi)['student']

student_name = student_detailed_info['first_name'] + ' ' + student_detailed_info['last_name']
room_id = student_detailed_info['room_id']

# Would be call to Rooms with school_id as parameter
r = open('rooms.json')
rooms = json.load(r)['rooms']

room_name = get_room_name(rooms, room_id)

print(room_name + ": " + "Please bring " + student_name + " to the front. Their parent is here to pick them up.")