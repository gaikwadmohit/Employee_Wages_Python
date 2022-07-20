import random

class Employee:
    def __init__(self, name,wage_per_hour,monthly_working_day):
        self.wage_per_hour = wage_per_hour
        self.monthly_working_day = monthly_working_day
        self.name = name
        self.employee_dict = {}

    def check_attendance(self,val):


            if val == 0:
                daily_work_hour = 8
                # print("Employee is present")
            elif val == 1:
                daily_work_hour = 4
                # print("Employee is present for part-time ")
            else:
                daily_work_hour = 0
                # print("Employee is absent ")
            return daily_work_hour

    def calculating_wage(self):

        try:
            total_wage = 0
            no_of_working_days = 0
            while no_of_working_days < self.monthly_working_day:
                no_of_working_days += 1
                rand = random.randint(0, 2)
                daily_work_hour = self.check_attendance(rand)
                daily_wage = self.wage_per_hour * daily_work_hour
                # print(f" The daily wage is : {daily_wage}")
                total_wage += daily_wage
            # print(f"The monthly wage is : {total_wage}")
            return total_wage

        except Exception as e:
            print(e)

class Company:
    def __init__(self, name):
        self.name = name
        self.employee_dict = {}

    def add_employee(self, emp):
        self.employee_dict.update({emp.name: emp})
        return self.employee_dict

    def get_employee(self, employee_name):
        emp_obj = self.employee_dict.get(employee_name)
        print(emp_obj.as_dict())
        return emp_obj

    def delete_employee(self, emp_name):
        self.employee_dict.pop(emp_name)
        return self.employee_dict

    def employee_details_view(self):
        for i,value in self.employee_dict.items():
            print(value.as_dict())
        return self.employee_dict


def add_company():
    comp = input("Enter company name : ")
    comp_obj = Company(comp)
    comp_dict.update({comp_obj.name: comp_obj})
    return comp_dict

def display_company():
    print(comp_dict)


def add_employee():
    c_name = input("Enter company name : ")
    comp_e = comp_dict.get(c_name)
    if comp_e is None:
        comp_e = Company(c_name)
        comp_dict.update({comp_e.name: comp_e})
    name = input("Enter employee name : ")
    emp = Employee(name, 50, 20)
    comp_e.add_employee(emp)


def get_employee():
    c_name = input("Enter company name : ")
    comp_e = comp_dict.get(c_name)
    if comp_e is None:
        print("Company doesn't exit ")
        return
    employee_name = input("Enter employee name : ")
    comp_e.get_employee(employee_name)


def delete_employee():
    c_name = input("Enter company name : ")
    comp_e = comp_dict.get(c_name)
    if comp_e is None:
        print("Company doesn't exit ")
        return
    emp_name = input("Enter employee name : ")
    comp_e.delete_employee(emp_name)


def display_employees():
    print("*************************************")
    company_name = input("Enter company name : ")
    comp_obj = comp_dict.get(company_name)
    if comp_obj is None:
        print("Company doesn't exit ")
        return
    comp_obj.employee_details_view()



if __name__ == "__main__":

    try:
        comp_dict = {}
        while True:
            print("1.add_company"
                  "\n2.Display Company"
                  "\n3.Add Employee"
                  "\n4.Get Employee"
                  "\n5.Delete Employee"
                  "\n6.display_employees"
                  "\n0.Exit")

            dict_e = {1: add_company,
                      2: display_company,
                      3: add_employee,
                      4: get_employee,
                      5: delete_employee,
                      6: display_employees}

            r = int(input("Enter a number : "))
            if r == 0:
                break
            dict_e.get(r)()
            input("Press enter to continue ")
            print("Please Choose following Option ")

    except Exception as e:
        print(e)


