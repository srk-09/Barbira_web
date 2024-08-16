class emp():
    def __init__(self,ename,eid,esalary):
        self.ename=ename
        self.eid = eid
        self.esalary = esalary

    def employee_details(self):
        print("Empname={} Empid={} Empsalary={}".format(self.ename,self.eid,self.esalary))
