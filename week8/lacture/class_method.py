class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    @classmethod
    def from_input(cls):
        name = input("Enter Name: ")
        house = input("Enter House: ")
        return cls(name, house)
    
def main():
    student = Student.from_input()
    print(student.name, student.house)
    
if __name__ == "__main__":
    main()