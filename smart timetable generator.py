import random

print("===== SMART TIMETABLE GENERATOR =====")

# Input subjects
n = int(input("Enter number of subjects: "))
subjects = []

for i in range(n):
    sub = input(f"Enter subject {i+1}: ")
    subjects.append(sub)

# Input days and lectures
days = int(input("Enter number of working days: "))
lectures = int(input("Enter lectures per day: "))

print("\n📅 Generated Timetable\n")

timetable = {}

for d in range(1, days + 1):
    daily_schedule = []
    last_subject = ""

    for l in range(lectures):
        available = [s for s in subjects if s != last_subject]
        subject = random.choice(available)
        daily_schedule.append(subject)
        last_subject = subject

    timetable[f"Day {d}"] = daily_schedule

# Display timetable
for day, schedule in timetable.items():
    print(day, ":", " | ".join(schedule))