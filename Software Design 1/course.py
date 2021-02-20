from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self,name,code,max_,min_,professor):
        self.name=name
        self.code=code
        self.max=max_
        self.min=min_
        self.professors=[]
        self.enrollments=[]


        if (isinstance(professor,professor)):
            self.professor.append(professor)
        elif  isinstance(professor,list):
            for entry in professor:
                if not isinstance(entry,professor):
                    raise Error("Invalid professor")
            self.professor=professor
        else:
            raise Error("Invalid professor")
    
    def add_professor(self,professor):
        if not isinstance(professor,professor):
            raise Error("Invalid Professor")
        self.professor.append(professor)
    def add_enrollment(self,enroll):
        if not isinstance(enroll,Enroll):
            raise  Error("Invalid Enrolment")
        if (len(enrollments)) == self.max:
            raise Error("Cannot Enroll, Course is full")
        self.enrollments.append(enroll)
    def is_cancelled(self):
        return len(self.enrollments) <self.min
