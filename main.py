from postgres import init, add_student, add_property, close, get_results


def main():
    conn, cursor = init(host='127.0.0.1', dbname='labs', user='postgres', password='postgres', port=5432)
        # input students

    students = int(input("Яку кількість студентів бажаєте додати?\n"))
    if students < 0:
        print("Введена кількість студентів повинна бути 1 і більше. Перевірте введенні вами дані")

    elif students == 0:
        res = get_results(cursor)
        print(res)
        close(cursor, conn)

    else:
        for i in range(students):
            name = str(input(f"\nВведіть ім'я {i+1} студента: "))
            dob = str(input(f"Введіть дату народження студента {i+1} (Y-М-D): "))
            students = add_student(cursor, name, dob)
                # input propertys

            propertyn = input(f"Скільки властивостей для студента {i+1} бажаєте додати? ->  ")
            if int(propertyn) < 0:
                print("Введена кількість записів повинна бути не мешою за нуль. Перевірте введенні вами дані")

            elif int(propertyn) == 0:
                print('pass')

            else:
                for j in range(int(propertyn)):
                    property = input(f"Введіть властивість {j+1} для студента {name}: ")
                    add_property(cursor, student_id=i, property=property)
        res = get_results(cursor)
        print(res)
        close(cursor, conn)


if __name__ == '__main__':
    main()
