class Employee:
    raise_amount = 1
    number_of_employee= 0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'@.com'
        Employee.number_of_employee+=1

    def fullname(self):
        print(f"{self.pay} of employee {self.first}")
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



class Developer(Employee):
    def __init__(self, first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

#print(Employee.number_of_employee)
dev_1 =Developer("john","desuza",400000,"python")
dev_2 =Developer("ram","patil",500000,"python")
#print(Employee.number_of_employee)

#print(emp_1)
print(dev_1.prog_lang)
print(dev_2.email)

#print(emp_1.fullname())
#print(Employee.fullname(emp_2))

