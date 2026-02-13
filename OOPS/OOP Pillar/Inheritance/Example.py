class Employee:         # parent class
    start_time = "9AM"
    end_time = "5PM"
class Teacher(Employee):         # child class
    def __init__(self, subject):
        self.subject = subject


t1 = Teacher("Data Science")
print(t1.subject, t1.start_time, t1.end_time)