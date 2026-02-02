#inheritance 
class Wizard:
    def __init__(self, name, age = None):
        self.name = name
        self.age = age
class Student(Wizard):
    def __init__(self, name, age, house):
        super().__init__(name, age)
        self.house = house
class Professor():
    def __init__(self, name, subject):
        # super().__init__(name)
        self.name = name
        self.subject = subject

def main():
    wizard = Wizard("ls")
    student = Student("pd",16,"griff")
    professor = Professor("sd", "health")

    print(student.name, student.age, student.house)
    print(wizard.name, wizard.age)
    print(professor.name, professor.subject)

if __name__ == "__main__":
    main()