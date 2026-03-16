# Timetable Generator

print("=== My Timetable ===")

# Days and subjects
timetable = {
    "Monday": "Maths",
    "Tuesday": "Physics",
    "Wednesday": "Chemistry",
    "Thursday": "Computer Science",
    "Friday": "English",
    "Saturday": "Sports"
}

# Display timetable
for day, subject in timetable.items():
    print(day, ":", subject)