my_list = [1, 3, "Michele", [5, 6, 7]]
for element in my_list:
  print(element)
  grade = input("Enter your grade: ")
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 65:
  print("D")
else:
  print("F")