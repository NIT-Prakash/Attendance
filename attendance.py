database = {
    1: {
        'name': 'aman',
        'roll': 1,
        'attendance': 60,
        'username': 'aman@gmail.com',
        'password': 123
    },
    2: {
        'name': 'sahil',
        'roll': 2,
        'attendance': 67,
        'username': 'sahil@gmail.com',
        'password': 234
    },
    3: {
        'name': 'ritika',
        'roll': 3,
        'attendance': 63,
        'username': 'ritika@gmail.com',
        'password': 345
    }
}

teacher_username = 'teacher@gmail.com'
teacher_password = '123456'

while 1:
    print("Main Menu")
    print("Press 1 if Teacher")
    print("Press 2 if Student")
    print("Press 3 to Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == teacher_username and password == teacher_password:
            print("*Welcome to Teacher Section*")
            while 1:
                print("Teacher Menu")
                print("Press 1 to modify attendance")
                print("Press 2 to view attendance")
                print("Press 3 to add student")
                print("Press 4 to see details of a student")
                print("Press 5 to logout")
                val = int(input("Enter your choice: "))
                if val == 1:
                    name = input("Enter name of student: ")
                    for i in database:
                        if name == database[i]['name']:
                            database[i]['attendance'] += 1
                            print(f"{name} marked present.")
                elif val == 2:
                    name = input("Enter name of student: ")
                    for i in database:
                        if name == database[i]['name']:
                            print(f"{name} : Attendance is : {database[i]['attendance']}")
                elif val == 3:
                    name = input("Enter name of new student: ")
                    rollno = len(database) + 1
                    uname = input("Enter username of new student: ")
                    psw = int(input("Enter password of new student: "))
                    atten = int(input("Enter attendance of new student: "))
                    
                    database[len(database) + 1] = {
                        'name': name,
                        'roll': rollno,
                        'attendance': atten,
                        'username': uname,
                        'password': psw
                    }
                    print("New student added successfully.")
                elif val == 4:
                    rollnum = int(input("Enter roll number of the student whose details you want to see: "))
                    print(database[rollnum])
                else:
                    print("Logging Out...")
                    break
        else:
            print("Invalid credentials.")
    elif ch == 2:
        username = input("Enter username: ")
        password = int(input("Enter password: "))
        logged_in_student = None
        for i in database:
            if username == database[i]['username'] and password == database[i]['password']:
                logged_in_student = database[i]
                break
        
        if logged_in_student:
            print("*Welcome to Student Section*")
            while 1:
                print("Student Menu")
                print("Press 1 to view attendance")
                print("Press 2 to logout")
                val = int(input("Enter your choice: "))
                if val == 1:
                    print(f"{logged_in_student['name']} : Your attendance is : {logged_in_student['attendance']}")
                elif val == 2:
                    print("Logging Out...")
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Invalid Credentials.")
    elif ch == 3:
        print("Exiting....")
        break
    else:
        print("Invalid choice.")