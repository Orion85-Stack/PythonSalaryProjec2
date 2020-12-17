name = input("Please enter your name: ")
name_second = input("Please enter your second name: ")
salary_list_names = []
salary_list_names.append(name.title())
salary_list_names.append(name_second.title())
print (f"Herewith the names on the salary list: \n\t{salary_list_names}")

hourly_rate_name = int(input(f"What is the hourly rate for {name}: "))
hourly_rate_name_second = int(input(f"What is the hourly rate for {name_second}: "))
salary_list_names_wages = []
salary_list_names_wages.append(hourly_rate_name)
salary_list_names_wages.append(hourly_rate_name_second)
print (salary_list_names_wages)
print (f"The hourly wage for {name} is: \n\t{hourly_rate_name} \nand for {name_second} is: \n\t{hourly_rate_name_second}.")
