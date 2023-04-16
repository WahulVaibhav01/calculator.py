first = int(input("Enter your first no :"))
operator = input("+ - * / % =")
second = int(input("Enter your second no:"))

if operator == "+":
  print(first + second)

elif operator == "-":
  print(second - first)

elif operator == "*":
  print(first * second)

elif operator == "/":
  print(first / second)

elif operator == "%":
  print(first % second)

else:
  print("Not found")
