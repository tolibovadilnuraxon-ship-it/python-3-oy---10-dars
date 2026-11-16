from student import students

def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print("Baho qo'shildi.")
    else:
        print("Talaba topilmadi.")

def average_grade(name):
    if name in students and students[name]:
        avg = sum(students[name]) / len(students[name])
        print(f"{name} ning o'rtacha bahosi: {avg:.2f}")
    else:
        print("Talaba topilmadi yoki baholari yo'q.")

def top_student():
    best_name = None
    best_avg = -1
    for name, grades in students.items():
        if grades:
            avg = sum(grades) / len(grades)
            if avg > best_avg:
                best_avg = avg
                best_name = name
    if best_name:
        print(f"Eng yuqori natija: {best_name} ({best_avg:.2f})")
    else:
        print("Baholangan talabalar yo'q.")
