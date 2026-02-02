# Example: Using @property and explaining _name, name, and self


# Example 1: Direct assignment to internal variables (does NOT use property setters)
class StudentDirect:
    def __init__(self, name, house):
        # Direct assignment: does NOT use property setters
        self._name = name
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        self._house = value

# Example 2: Assignment via property setters (RECOMMENDED if you want validation/logic)
class Student:
    def __init__(self, name, house):
        # Assignment via property: uses the setter, so any logic/validation in the setter runs
        self.name = name
        self.house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # You can add validation here if needed
        self._name = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        # You can add validation here if needed
        self._house = value

    # The @property decorator makes this method accessible as an attribute
    @property
    def name(self):
        # self refers to the current object instance
        # self._name accesses the internal variable
        return self._name

    # The setter allows you to set the value using student.name = value
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        self._house = value

# Usage:
print("--- StudentDirect (no property setters in __init__) ---")
student1 = StudentDirect("Harry", "Gryffindor")
print(student1.name)      # 'Harry'
student1.name = "Ron"     # Calls setter
print(student1.name)      # 'Ron'
print(student1._name)     # Direct access

print("--- Student (uses property setters in __init__) ---")
student2 = Student("Hermione", "Gryffindor")
print(student2.name)      # 'Hermione'
student2.name = "Luna"    # Calls setter
print(student2.name)      # 'Luna'
print(student2._name)     # Direct access

# Summary:
# - If you assign self._name in __init__, the property setter is NOT used.
# - If you assign self.name in __init__, the property setter IS used.
# - Use student.name outside the class (safe, can add logic/validation)
# - Use self._name inside the class to refer to the internal variable
# - Avoid using student._name outside the class

# self always refers to the current object, allowing access to its data and methods
'''
class Student:
    def __init__(self, name, house):

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house


    def __str__(self):
        return(f"{self.name} from {self.house}")
    
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main():
    student = get_student()
    print(student._name)



def get_student(): 
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

'''
    