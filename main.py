#Класи
class Student:
    count = 0
    def __init__(self , height = 150):
        self.height = height
        Student.count += 1
Oleg = Student()
print(f'Олег: {Oleg.height} см')
masha = Student(173)
print(f"Маша: {masha.height} см")
print("Кількість обєктів:" , Student.count)
