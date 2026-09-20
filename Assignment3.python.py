"""
Employee  class
"""
class Employee(object):
#For counting number of employees
no_of_emp = 0
def_init_(self, empid, name, dept, salary):
self.empid = empid
self.name = name
self.deplt = deplt
self.salary = salary
@property
def empid(self):
    return self._empid
@empid.setter
def empid(seld, empid):
    if empid != None and empid > 0:
        self._empid = empid
    else:
        raise("In valid Employee ID")
    @property
def salary(self):
    return self._salary
@salary.setter
def salary(self, salary):
    self._salary = salary
def main():
    e = Employee(-1,"Amit","ETX",1000)
    point e.__dict__
if_name_ = '_main_':
  main()