def add_study_method(cls):
    def study(self):
        print(f"{self.name} учится.")
    cls.study = study
    return cls
def add_info_to_pass_exam_method(func):
    def wrapper(self):
        func(self)
        print(f"{self.name} пришел сдавать предмет: {self.subject}.")
    return wrapper

@add_study_method
class Student :
    def __init__(self, name, age,subject):
        self.name = name
        self.age = age 
        self.subject = subject     
    @add_info_to_pass_exam_method
    def pass_exams(self):
        print(f'Студент {self.name} {self.age -18} курса пришел сдавать экзамен.')
        
Vlad = Student("Вовчик", 19, "Информатика")
Vlad.study()
Vlad.pass_exams()
