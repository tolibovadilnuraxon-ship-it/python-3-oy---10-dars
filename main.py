from student import add_student, show_students, search_student
from grades import add_grade, average_grade, top_student

while True:
    print("\n1. Talaba qo'shish")
    print("2. Barcha talabalarni chiqarish")
    print("3. Talaba qidirish")
    print("4. Baho qo'shish")
    print("5. O'rtacha bahoni hisoblash")
    print("6. Eng yuqori baho olgan talaba")
    print("0. Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        ism = input("Talaba ismi: ")
        add_student(ism)
    elif tanlov == "2":
        show_students()
    elif tanlov == "3":
        ism = input("Qidirilayotgan ism: ")
        search_student(ism)
    elif tanlov == "4":
        ism = input("Talaba ismi: ")
        baho = float(input("Baho: "))
        add_grade(ism, baho)
    elif tanlov == "5":
        ism = input("Talaba ismi: ")
        average_grade(ism)
    elif tanlov == "6":
        top_student()
    elif tanlov == "0":
        break
    else:
        print("Noto'g'ri tanlov!")
