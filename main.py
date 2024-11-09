
from people import Faculty, Student

faculty_list = []
student_list = []

def add_faculty():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    department = input("Enter department: ")
    faculty_list.append(Faculty(firstname, lastname, department))

def print_faculty():
    print("\n======================= FACULTY =======================")
    print("Record  Name                  Department")
    print("======  ====================  =========================")
    for idx, faculty in enumerate(faculty_list):
        print(f"{idx:<7} {faculty.firstname} {faculty.lastname:<20} {faculty.department}")

def add_student():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    classyear = input("Enter class year: ")
    major = input("Enter major: ")
    print("Select faculty advisor by record number:")
    print_faculty()
    advisor_index = int(input("Enter faculty advisor record number: "))
    
    student = Student(firstname, lastname)
    student.set_class(classyear)
    student.set_major(major)
    if 0 <= advisor_index < len(faculty_list):
        student.set_advisor(faculty_list[advisor_index])
    student_list.append(student)

def print_students():
    print("\n===================================== STUDENTS ======================================")
    print("Name                  Class      Major                      Advisor")
    print("====================  =========  =========================  =========================")
    for student in student_list:
        advisor_name = f"{student.advisor.firstname} {student.advisor.lastname}" if student.advisor else "None"
        print(f"{student.firstname} {student.lastname:<20} {student.classyear:<10} {student.major:<26} {advisor_name}")

def main():
    while True:
        print("\n      *** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
        print("1. Add faculty")
        print("2. Print faculty")
        print("3. Add student")
        print("4. Print student")
        print("9. Exit the program")
        
        choice = input("Enter menu choice: ")
        
        if choice == '1':
            add_faculty()
        elif choice == '2':
            print_faculty()
        elif choice == '3':
            add_student()
        elif choice == '4':
            print_students()
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
