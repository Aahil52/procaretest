import json
from datetime import datetime


# Returns the most recent student id to be signed out
def get_last_sign_out(students_attendance):
    sign_out_times = [(student['student_id'], datetime.strptime(student['sign_out_time'], '%Y-%m-%d %H:%M'))
                       for student in students_attendance]
    sign_out_times.sort(key=lambda x: x[1], reverse = True)
    return sign_out_times[0][0]

def get_room_name(rooms, id):
    for room in rooms:
        if room['id'] == id:
            return room['name']

def get_lso_room_and_name():
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

    return {'student_name': student_name, 'room_name': room_name}

last_sign_out = get_lso_room_and_name()

print(f"{last_sign_out['student_name']}: Please bring {last_sign_out['student_name']} to the front. Their parent is here to pick them up.")