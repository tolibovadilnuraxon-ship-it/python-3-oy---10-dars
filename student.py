students = {}

def add_student(name):
    if name not in students:
        students[name] = []
        print("Talaba qo'shildi.")
    else:
        print("Bu talaba mavjud.")

def show_students():
    if not students:
        print("Talabalar ro'yxati bo'sh.")
    else:
        for name in students:
            print(name)

def search_student(name):
    if name in students:
        print(f"Topildi: {name}, Baholari: {students[name]}")
    else:
        print("Talaba topilmadi.")
