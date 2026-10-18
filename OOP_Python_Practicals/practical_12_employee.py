
class Employee:
    count = 0

    def __init__(self, emp_no, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            raise SystemExit("Error: Basic, DA and HRA cannot be negative.")

        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra

        Employee.count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        if hasattr(self, "emp_no"):
            Employee.count -= 1

    def __str__(self):
        return (
            f"Employee Number: {self.emp_no}\n"
            f"Name: {self.name}\n"
            f"Department: {self.dept}\n"
            f"Basic Salary: {self.basic}\n"
            f"DA: {self.da}\n"
            f"HRA: {self.hra}\n"
            f"Total Salary: {self.salary()}"
        )


emp1 = Employee(101002, "Subham Singh", "Bsc(hons)CS", 20000, 5000, 3000)

print(emp1)
print("Total employee objects:", Employee.count)
