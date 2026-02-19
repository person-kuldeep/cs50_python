students = ["harry", "hitesh", "david"]

coders =  {student:"coder" for student in students}
l_coders = [{"name":student,"house" :"coders"} for student in students]
print(type(coders))
print(type(l_coders))
print(l_coders)
print(coders)