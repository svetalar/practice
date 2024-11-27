'''ИЗД 6, Звонков А.А., гр. 3587'''

from student import Student
from group import Group 

print(__doc__)


group_number = input("Введите номер группы: ")
group = Group(group_number)

while True:
    print("\n1. Добавить студента")
    print("2. Удалить студента")
    print("3. Показать список студентов")
    print("4. Выход")
    choice = input("Выберите действие: ")

    if choice == '1':
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        second_name = input("Введите отчество: ")
        
        group.add_student(last_name, first_name, second_name)
    
    elif choice == '2':
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        second_name = input("Введите отчество: ")
        group.del_student(last_name, first_name, second_name)
    
    elif choice == '3':
        print("Список студентов:")
        group.list_students()
    
    elif choice == '4':
        break
    
    else:
        print("Неверный выбор, попробуйте снова.")

print(group)

 