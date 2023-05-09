#симулятор база данніх
class School:
    def __init__(self , name , students):
        self.name = name
        self.students = students   #список студентів
    def admit_student(self , student): #додавання студентів
        self.students.append(student)
        print(f"{student.name} був доданий до школи {self.name}")  #дописати
    def expel_student(self , student): # видалення студента
        expelled_student = next(filter(lambda s : s.name == student.name and s.grade == student.grade , self.students) , None)
        if expelled_student is not None:
           self.students.remove(expelled_student)
           print(f"{expelled_student.name} був видалений с {self.name}")
        else:
           print(f"{student.name} не був знайдений  {self.name}")




class Student:
    def __init__(self , name , grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade += 1
        print(f"{self.name} був підвіщений {self.grade}")
    def demote(self):
        self.grade -= 1
        print(f"{self.name} був понижений {self.grade}")
    def __str__(self):
        return f"{self.name} - Ранг {self.grade}"   #додали метод виводу


lisa = Student("Alisa" , 6)
masha = Student("Masha" , 2)
dasha = Student("Dasha" , 50)
dima = Student("Dmutro" , 23)
gleb = Student("Gleb" , 100)
my_school = School("ItStep" , [lisa , masha , dasha , dima , gleb])
print(f"Початкові студенти")
for student in my_school.students:
    print(student)

print("Оновлення")
my_school.admit_student(Student("Bogdan" , 3))
my_school.expel_student(Student("Alisa" , 6))





multiply = lambda x , y : x * y
print(multiply(5 , 4))

number = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
filtered_number = list(filter(lambda x : x % 2 == 0 , number))
print(filtered_number)