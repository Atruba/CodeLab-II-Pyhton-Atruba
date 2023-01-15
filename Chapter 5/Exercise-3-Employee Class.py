class Employee:
    def __init__(self, eid=None, Name=None, Age=None, Salary=None):
        self.name = Name
        self.age = Age
        self.id = eid
        self.salary = Salary

    def __str__(self):
        return f"Name: {self.name}, {self.age}, {self.id}, {self.salary}"

    def set_data(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.id = int(input("Enter your id: "))
        self.salary = int(input("Enter your salary: "))

if __name__ == '__main__':
    employees = []
    for i in range(5):
        emp = Employee()
        emp.set_data()
        employees.append(emp)

    for emp in employees:
        print(emp)