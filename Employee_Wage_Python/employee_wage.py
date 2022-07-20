import random

class EmployeeWage:
    def employee(self):

        try:
            rand = random.randint(0, 1)
            if rand == 0:
                print("Employee is present")
            else:
                print("Employee is absent")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        obj = EmployeeWage()
        obj.employee()
    except Exception as e:
        print(e)
