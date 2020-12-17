name = input("Please enter your name: ")
name_second = input("Please enter your second name: ")
salary_list_names = []
salary_list_names.append(name.title())
salary_list_names.append(name_second.title())
print(f"Herewith the names on the salary list: \n\t{salary_list_names}")

# add the float to the input
hourly_rate_name = float(input(f"What is the hourly rate for {name.title()}: "))
hourly_rate_name_second = float(input(f"What is the hourly rate for {name_second.title()}: "))
salary_list_names_wages = []
salary_list_names_wages.append(hourly_rate_name)
salary_list_names_wages.append(hourly_rate_name_second)
print(salary_list_names_wages)
print(
    f"The hourly wage for {name.title()} is: \n\t{hourly_rate_name} "
    f"\nand for {name_second.title()} is: \n\t{hourly_rate_name_second}."
)

# add the float to the input
name_worked_hours = float(input(f"How many hours did {name} work this week? "))
name_second_worked_hours = float(input(f"How many hours did {name_second} work this week? "))

# this calculates the first wage to be paid
print(
    f"{name.title()} has worked {name_worked_hours} hours for the week and should be paid: "
    f"\n\t{name_worked_hours * hourly_rate_name}"
)

# this calculates the second wage to be paid
print(
    f"{name_second.title()} has worked {name_second_worked_hours} hours for the week and should be paid: "
    f"\n\t{name_second_worked_hours * hourly_rate_name_second}"
)
