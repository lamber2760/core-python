class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
p = programmer("Lucky",12000000,176056)
print(p.company,p.name,p.pincode,p.salary)

r= programmer("sachin",12000000,176056)
print(r.company,r.name,r.pincode,r.salary) 