import sqlite3
from faker import Faker
from datetime import date
from random import random, randint


fake = Faker(locale='uk_UA')

def create_all_tables(students_in_group=10,days=4,min_count_ball=5,max_count_ball=20):
    cursor.execute("DROP TABLE IF EXISTS  students")
    cursor.execute("DROP TABLE IF EXISTS  groups")
    cursor.execute("DROP TABLE IF EXISTS  teachers")
    cursor.execute("DROP TABLE IF EXISTS  subjects")
    cursor.execute("DROP TABLE IF EXISTS  grades")

    create_table_students=("CREATE TABLE students ("
                           "id INTEGER PRIMARY KEY AUTOINCREMENT  ,"
                           " name varchar(50) NOT NULL ,"
                           " id_groups int )"
                           )
    create_table_groups = "CREATE TABLE groups (id int PRIMARY KEY, name varchar(3) )"

    create_table_teachers=("CREATE TABLE teachers ("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT  ,"
                        " name varchar(50) NOT NULL )"
                        )
    create_table_subjects = ("CREATE TABLE subjects ("
                             "id INTEGER PRIMARY KEY AUTOINCREMENT  ,"
                             " name varchar(30) NOT NULL,"
                             "id_teacher int NOT NULL)"
                           )
    create_table_grades = ("CREATE TABLE grades ("
                             "date DATE NOT NULL ,"
                             " id_stud int NOT NULL,"
                             "id_sub int NOT NULL,"
                             "grade int NOT NULL)"
                           )




    cursor.execute(create_table_students)
    cursor.execute(create_table_groups)
    cursor.execute(create_table_teachers)
    cursor.execute(create_table_subjects)
    cursor.execute(create_table_grades)

#----------------insert to students-------------------------

    for _ in range(students_in_group):
        name_s = fake.first_name() + " " + fake.last_name()
        cursor.execute(f"""INSERT INTO students (name, id_groups) VALUES ('{name_s}', 1)""")

    for _ in range(students_in_group):
        name_s = fake.first_name() + " " + fake.last_name()
        cursor.execute(f"""INSERT INTO students (name, id_groups) VALUES ('{name_s}', 2)""")

    for _ in range(students_in_group):
        name_s = fake.first_name() + " " + fake.last_name()
        cursor.execute(f"""INSERT INTO students (name, id_groups) VALUES ('{name_s}', 3)""")

    # ----------------insert to groups-------------------------

    cursor.execute("INSERT INTO groups (id, name) VALUES (1,'Group21'), (2,'Group22'), (3,'Group23')")

    # ----------------insert to teachers-------------------------

    for _ in range(4):
        name_t = fake.first_name() + " " + fake.last_name()
        cursor.execute(f"""INSERT INTO teachers (name) VALUES ('{name_t}')""")

    # ----------------insert to subjects-------------------------
    cursor.execute("INSERT INTO subjects (name, id_teacher) VALUES ('English', 1), ('Python',2),"
               "('JS',3),('HTML',4), ('C++',2),('CSS',4),('Astronomy',3)")

    # ----------------insert to grades-------------------------
    for d in range(days):
        date_gr = date(2024, 3, 1 + d)

        for _ in range(randint(min_count_ball,max_count_ball)):
            if date_gr.weekday()<5:
                cursor.execute(f"""INSERT INTO grades (date, id_stud, id_sub, grade) VALUES ('{date_gr}', {randint(1, students_in_group*3)}, {randint(1, 7)}, {randint(3, 12)})""")

def select_all_student():
    cursor.execute("SELECT * FROM students")
    print(f'\ntable Students')
    print("-" * 60)
    for line in cursor.fetchall():
        print(f'{line[0]}) {line[1]}; group - {line[2]}')
    print("*" * 60)

def select_all_groups():
    cursor.execute("SELECT * FROM groups")
    print(f'\ntable Groups')
    print("-" * 60)
    for line in cursor.fetchall():
        print(f'{line[0]}) {line[1]}')
    print("*" * 60)
def select_all_teachers():
    cursor.execute("SELECT * FROM teachers")
    print(f'\ntable Teachers')
    print("-" * 60)
    for line in cursor.fetchall():
        print(f'{line[0]}) {line[1]}')
    print("*" * 60)

def select_all_subjects():
    cursor.execute("SELECT * FROM subjects")
    print(f'\ntable subjects')
    print("-" * 60)
    for line in cursor.fetchall():
        print(f'{line[0]}) {line[1]}; ID викладача: {line[2]}')
    print("*" * 60)
def select_all_grades():
    cursor.execute("SELECT * FROM grades")
    print(f'\ntable grades')
    print("-" * 60)
    n=0
    for line in cursor.fetchall():
        n+=1
        print(f'{n}) {line[0]} - ID студента {line[1]}; ID предмета: {line[2]}; оцінка: {line[3]}')
    print("*" * 60)

def select_1():
    with open("select1.sql") as sql:
        cursor.execute(sql.read())
    print('5 студентів з найвищими середніми оцінками')
    print("-" * 50)
    for line in cursor.fetchall():
        print(f'{line[0]})  середній бал студента {line[2]}  -  {line[1]}')
        #pass
    print("-" * 50)

def  select_2():
   id_pred = input("введіть номер предмета:>>>")
   with open("select2.sql") as sql:
       cursor.execute(sql.read(), id_pred)
   print("-" * 50)
   for line in cursor.fetchall():
       print(f'{line[0]})  середній бал студента {line[2]}  -  {line[1]} по предмету- {line[3]}')


   with open("select2a.sql") as sql:
       cursor.execute(sql.read(), id_pred)
   for line in cursor.fetchall():
       print(f'***** - максимальний середній бал по предмету- {line[3]} у студента ({line[0]}) {line[2]}  -  {line[1]} ')

def select_3():
    print("-" * 50)
    print('*********середній бал у групах з певного предмета***********')
    id_pred = input("введіть номер предмета:>>>")
    with open("select3.sql") as sql:
        cursor.execute(sql.read(), id_pred)
    print("-" * 50)
    for line in cursor.fetchall():
        print(f'середній бал по предмету {line[2]}  у групі {line[0]}  -  {line[1]} ')

def select_4():
     with open("select4.sql") as sql:
         cursor.execute(sql.read())
     print("-" * 50)
     for line in cursor.fetchall():
         print(f'середній бал по всім оцінкам  у потоці  - {line[0]} ')
def select_5():
    print("-" * 50)
    name = input("введіть повне імя(або частину) викладача:>>>")
    with open("select5.sql") as sql:
        cursor.execute(sql.read(),(f'%{name}%',))
    for line in cursor.fetchall():
        print(f"викладач {line[1]} читає {line[0]}")
    print("-" * 50)
def select_6():
    print('****************** Список студентів групи *****************')
    print("-" * 50)
    gr = input("введіть номер групи:>>>")

    with open("select6.sql") as sql:
        cursor.execute(sql.read(), f'{gr}')
    print(f'список студентів гр №{gr}')
    n = 0
    for line in cursor.fetchall():
        n += 1
        print(f'{n}) {line[0]} ')
    print("-" * 50)

def select_7():
    print('****************** оцінки в групі по данному предмету *****************')
    print("-" * 50)
    gr = input("введіть номер групи:>>>")
    sb = input("введіть назву предмета:>>>")

    with open("select7.sql") as sql:
        cursor.execute(sql.read(), (f'{sb}', f'{gr}'))

    print(f'оцінки студентів {gr} групи  по предмету {sb} ')
    for line in cursor.fetchall():
        print(f"cтудент {line[0]}- оцінка {line[1]}")
    print("-" * 50)

def select_8():
    print('****************** які оцінки ставить викладач Х *****************')
    print("-" * 50)
    name = input("введіть повне імя (або частину) викладача:>>>")

    with open("select8.sql") as sql:
        cursor.execute(sql.read(), (f'%{name}%',))

    for line in cursor.fetchall():
        print(f"викладач {line[0]}- ставить в середньому оцінку {line[1]}")
    print("-" * 50)

def select_9():
    print('****************** На які предмети ходить студент Х *****************')
    print("-" * 50)
    name = input("введіть повне імя (або частину) студента:>>>")

    with open("select9.sql") as sql:
        cursor.execute(sql.read(), (f'%{name}%',))

    for line in cursor.fetchall():
        print(f"студент {line[0]}- має оцінки по предмету {line[1]}")
    print("-" * 50)

def select_10():
    print("++++++++Список курсів, які певному студенту читає певний викладач.++++++++++")

    name_p = input("введіть повне імя (або частину) викладача:>>>")
    name_s = input("введіть повне імя (або частину) cстудента:>>>")
    print("-" * 50)

    with open("select10.sql") as sql:
        cursor.execute(sql.read(), (f'%{name_p}%',f'%{name_s}%'))

    for line in cursor.fetchall():
        print(f"викладач {line[1]} читає {line[2]} студенту {line[0]} ")
    print("-" * 50)

def select_11():
    print("++++++++Середній бал, який певний викладач ставить певному студентові++++++++++")

    name_p = input("введіть повне імя (або частину) викладача:>>>")
    name_s = input("введіть повне імя (або частину) cстудента:>>>")
    print("-" * 50)

    with open("select11.sql") as sql:
        cursor.execute(sql.read(), (f'%{name_p}%', f'%{name_s}%'))

    for line in cursor.fetchall():
        print(f"викладач {line[1]} ставить середній бал {line[2]} студенту {line[0]} ")
    print("-" * 50)

def select_12():
    print('****************** оцінки в групі по данному предмету на останньому занятті*****************')
    print("-" * 50)
    gr = input("введіть номер групи:>>>")
    sb = input("введіть назву предмета:>>>")

    with open("select12.sql") as sql:
        cursor.execute(sql.read(), (f'{sb}', f'{gr}'))

    print(f'оцінки студентів {gr} групи  по предмету {sb} ')
    for line in cursor.fetchall():
        print(f"cтудент {line[0]}- оцінка {line[1]}  на занятті {line[2]} ")
    print("-" * 50)

with sqlite3.connect("universy.db") as conn:
    cursor=conn.cursor()
    create_all_tables(5,5,6,12)   # включити якщо захочеться змінити базу, відключити якщо ні

    select_all_student()  # вивести списо всіх студентів
    select_all_groups()   # вивести список всіх груп
    select_all_teachers()  ## вивести список всіх викладачів
    select_all_subjects()  # вивести список всіх предметів
    select_all_grades()  # вивести всі оцінки за весь період

    select_1() # 5 найвищих Cередні бали студентів по всім предметам_
    select_2()  # __max Cередній бали по предмету_
    select_3() # Cередній бали по предмету в групі_
    select_4() # Cередній бал по всім оцінкам_
    select_5() # Які предмети читає викладач
    select_6() #список студентів однієї групи_
    select_7() # оцінки студентів групи з певного предмета________________
    select_8() # середній бал, який ставить певний викладач зі своїх предметів___
    select_9() # Предмети по яким студент має оцінки
    select_10() #Список курсів, які певному студенту читає певний викладач.
    select_11()# Середній бал, який певний викладач ставить певному студентові
    select_12() #Оцінки студентів у певній групі з певного предмета на останньому занятті.












