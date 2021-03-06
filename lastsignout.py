import json
from datetime import datetime


# Returns the most recent student id to be signed out
def get_last_sign_out(students_attendance):
    sign_out_times = [(student['student_id'], datetime.strptime(student['sign_out_time'], '%Y-%m-%d %H:%M'))
                       for student in students_attendance]
    last_sign_out = max(sign_out_times, key=lambda x: x[1])
    return last_sign_out[0]

def get_room_name(rooms, target_id):
    for room in rooms:
        if room['id'] == target_id:
            return room['name']

# Would be call to Students Attendance with school_id as parameter
with open('students_attendance.json') as sa:
    students_attendance = json.load(sa)['attendance']
student_id = get_last_sign_out(students_attendance)

# Would be call to Student Detailed Info with student_id and school_id as parameter
with open(f'student_detailed_info/{student_id}.json') as sdi:
    student_detailed_info = json.load(sdi)['student']
student_name = f"{student_detailed_info['first_name']} {student_detailed_info['last_name']}"
room_id = student_detailed_info['room_id']

# Would be call to Rooms with school_id as parameter
with open('rooms.json') as r:
    rooms = json.load(r)['rooms']
room_name = get_room_name(rooms, room_id)

print(f"{room_name}: Please bring {student_name} to the front. Their parent is here to pick them up.")