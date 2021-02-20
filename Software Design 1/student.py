from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self,firs,last,dob,phone,address,internatinal=False):
        super().__init__(self,firs,last,dob,phone,address)
        self.internatinal=internatinal
        self.enrolled=[]

    def add_enrollment(self,enrol):
        if not isinstance(enroll,Enroll):
            raise  Error("Invalid Enroll")
        self.enrolled.append(enroll)
    def is_on_probation(self):
        return False
    
    def is_part_time(self):
        return len(self.enrolled) <= 3