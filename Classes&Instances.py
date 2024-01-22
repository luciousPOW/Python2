class Employee:
    def __init__(self, firstn, lastn, pay):
        self.firstn = firstn
        self.lastn = lastn
        self.pay = pay
        self.email = firstn + "." + lastn + '@company.com'
        

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.firstn = 'Louwis'
emp_1.lastn = 'Nabayan'
emp_1.email = 'nabayan.louwisalfred@gmail.com'
emp_1.pay = 50000

emp_2.firstn = 'Bibeng'
emp_2.lastn = 'Nabayan'
emp_2.email = 'ngitpa.bibeng.com'
emp_2.pay = 500000

print(emp_1.firstn)
print(emp_2.firstn)