import json
from datetime import datetime


def get_last_sign_out(students_attendance):
    sign_out_times = []
    for student in students_attendance:
        sot_obj = datetime.strptime(student['sign_out_time'], '%Y-%m-%d %H:%M')
        sign_out_times.append((student['student_id'], sot_obj))
    sign_out_times.sort(key=lambda x: x[1], reverse = True)
    return sign_out_times[0][0]

def get_room_name(rooms, id):
    for room in rooms:
        if room['id'] == id:
            return room['name']

# Would be call to Students Attendance with school_id as parameter
sa = open('students_attendance.json')
students_attendance = json.load(sa)['attendance']

student_id = get_last_sign_out(students_attendance)

# Would be call to Student Detailed Info with student_id and school_id as parameter
sdi = open(f'student_detailed_info/{student_id}.json')
student_detailed_info = json.load(sdi)['student']

student_name = f"{student_detailed_info['first_name']} {student_detailed_info['last_name']}"
room_id = student_detailed_info['room_id']

# Would be call to Rooms with school_id as parameter
r = open('rooms.json')
rooms = json.load(r)['rooms']

room_name = get_room_name(rooms, room_id)

print(f"{room_name}: Please bring {student_name} to the front. Their parent is here to pick them up.")