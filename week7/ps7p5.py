def calc_tuition(student_credit_hours, district_code):
    if district_code.upper() == 'I':
        return student_credit_hours * 250
    elif district_code.upper() == 'O':
        return student_credit_hours * 550
    else:
        return 0.0

def main():
    total_students_tuition = 0.0

    while True:
        student_user_input = input("Do you want to do the program? (Yes or No): ")
        if student_user_input.lower() != 'yes':
            break

        student_last_name = input("Enter student last name: ")
        while True:
            try:
                student_credit_hours = int(input("Enter credit hours: "))
                if student_credit_hours >= 0:
                    break
                else:
                    print("Credit hours cannot be negative. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number for credit hours.")

        district_code = input("Enter district code (I for in-district, O for out-of-district): ")

        student_tuition = calc_tuition(student_credit_hours, district_code)

        print(f"\nStudent: {student_last_name}")
        print(f"Tuition Owed: ${student_tuition:.2f}")

        total_students_tuition += student_tuition

    print(f"\nTotal tuition for all students: ${total_students_tuition:.2f}")

if __name__ == "__main__":
    main()
