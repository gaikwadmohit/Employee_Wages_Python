
import random


class Employee:
    def __init__(self, name, wage_per_hour, monthly_working_day, total_working_hour):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.monthly_working_day = monthly_working_day
        self.total_working_hour = total_working_hour

    def check_attendance(self, rand):


            if rand == 0:
                daily_work_hour = 8
                print(" Employee is present ")
            elif rand == 1:
                daily_work_hour = 4
                print(" Employee is present for part-time ")
            else:
                daily_work_hour = 0
                print(" Employee is absent ")
            return daily_work_hour


    def calculating_wage(self):

        try:
            total_wage = 0
            no_of_working_days = 0
            working_hours = 0
            while no_of_working_days < self.monthly_working_day and working_hours <= self.total_working_hour:
                no_of_working_days += 1
                rand = random.randint(0, 2)
                daily_work_hour = self.check_attendance(rand)
                print(f" The working days is : {no_of_working_days}")
                working_hours += daily_work_hour
                print(f" The working hours is : {working_hours}")
                daily_wage = self.wage_per_hour * daily_work_hour
                print(f" The daily wage is : {daily_wage}")
                total_wage += daily_wage
                print("------------------------------------------------")
            print(f"The monthly wage is : {total_wage}")
            print("------------------------------------------------")
            return total_wage

        except Exception as e:
            print(e)

    def as_dict(self):
        return {"Name": self.name, "Total_wage": self.calculating_wage()}


class Company:
    def __init__(self, name):
        self.name = name
        self.employee_dict = {}

    def add_employee(self, employee_obj):
        self.employee_dict.update({self.name: employee_obj})

    def get_employee(self, employee_name):
        return self.employee_dict.get(employee_name)

    def delete_employee(self):
        self.employee_dict.clear()

    def view(self):
        print(self.employee_dict)


if __name__ == "__main__":
    try:
        comp1 = Company("labz")
        comp2 = Company("tcs")

        company_dict = {comp1.name: comp1, comp2.name: comp2}


        while True:
            print(" ------------------------------------------------------------------------------ ")
            print("1.Add Employee\n2.Update Employee\n3.Delete Employee\n4.View\n5.Exit")
            ch = int(input("Enter choice : "))
            if ch == 1:
                comp_name = input("Search company name : ")
                comp_obj = company_dict.get(comp_name)
                name = input("Enter employee name : ")
                emp_obj = Employee(name, 20, 20, 100)
                comp1.employee_dict.update({emp_obj.name: emp_obj})
                print(" <<<<<<<<<<<<<<----->>>>>>>>>>>>>>>>>>> ")
            elif ch == 2:
                pass

            elif ch == 3:
                comp1.delete_employee()
            elif ch == 4:
                comp1.view()
                employee_name = input("Search employee name : ")
                obj = comp_obj.get_employee(employee_name)
                print(obj.as_dict())
            elif ch == 5:
                break
            else:
                print("Enter valid choice")

    except Exception as e:
        print(e)
