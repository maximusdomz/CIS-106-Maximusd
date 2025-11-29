def calc_pay(job_code, hours_worked):
    pay_rate = 0
    if job_code == 'L':
        pay_rate = 25
    elif job_code == 'A':
        pay_rate = 30
    elif job_code == 'J':
        pay_rate = 50
    else:
        print("Invalid Job Code entered.")
        return 0, 0

    employee_gross_pay = 0
    if hours_worked <= 40:
        employee_gross_pay = hours_worked * pay_rate
    else:
        overtime_hours = hours_worked - 40
        employee_gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)

    return pay_rate, employee_gross_pay

def main():
    total_employee_gross_pay = 0
    run_program = input("Do you want to process employee payroll? (Yes/No): ").strip().lower()

    while run_program == 'yes':
        employee_last_name = input("Enter employee's last name: ").strip()
        job_code = input("Enter job code (L, A, or J): ").strip().upper()

        try:
            hours_worked = float(input("Enter hours worked: "))
            if hours_worked < 0:
                print("Hours worked cannot be a negative number. Please re-enter.")
                continue
        except ValueError:
            print("Input for hours worked is invalid. Please enter a valid number.")
            continue

        pay_rate, employee_gross_pay = calc_pay(job_code, hours_worked)

        if pay_rate > 0:
            print(f"\nEmployee: {employee_last_name}")
            print(f"Hours Worked: {hours_worked}")
            print(f"Pay Rate: ${pay_rate:.2f}/hr")
            print(f"Gross Pay: ${employee_gross_pay:.2f}")
            total_employee_gross_pay += employee_gross_pay

        run_program = input("\nDo you want to process another employee? (Yes/No): ").strip().lower()

    print(f"\nTotal Gross Pay for all employees: ${total_employee_gross_pay:.2f}")


if __name__ == "__main__":
    main()