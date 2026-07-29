students = []
subjects_set = set()
print("Welcome to the student data organiser!")
while True:
    print("\nSelect an option: ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter Student Details:")
        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")

        subjects = input("Subjects (comma-separated): ").split(",")
        subjects = [subject.strip() for subject in subjects]
        student_info = (student_id,dob)

        student = {
            "id": student_id,
            "info": student_info,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }
        students.append(student)
        for subject in subjects:
            subjects_set.add(subject)
        print("\nStudent added successfully!")
    elif choice == "2":
        print("\nDisplay All Students")
        if len(students) == 0:
            print("No Student Record found.")
        else:
            for student in students:
                print(
                    f"Student Id: {student['id']} |"
                    f"Name: {student['name']} |"
                    f"Age: {student['age']} |"
                    f"Grade: {student['grade']} |"
                    f"Subjects: {','.join(student['subjects'])}"
                )
    elif choice == "3":
        update_id = int(input("\nEnter Student ID to update: "))
        found = False
        for student in students:
            if student["id"] == update_id:
                found = True
                student["age"] = int(input("Enter new age:"))
                new_subjects = input("Enter new subjects (comma-separated):").split(",")
                new_subjects = [subjects.strip() for subjects in new_subjects]
                student["subjects"] = new_subjects
                for subject in new_subjects:
                    subjects_set.add(subject)
                print("Student Information updated successfully!")
                break
            if not found:
                print("Student ID not found.")   
    elif choice == "4":
        delete_id = int(input("\nEnter student ID to delete: "))
        found = False 
        for i in range(len(students)):
            if students[i]["id"] == delete_id:
                found == True
                print("Student deleted successfully!")
                break
            if not found:
                print("Student not found.")
    elif choice == "5":
        print("\n Subjects Offered")
        if len(subjects_set) == 0:
            print("No subjects available.")
        else:
            for subject in subjects_set:
                print(subject)
    elif choice == "6":
        print("\nThank you for using the Student Data Organaiser!")
        break
    else:
        print("Invalid Choice.Please try again.")