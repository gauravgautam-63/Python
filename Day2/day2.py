"""print(10 > 9)
print(10 == 9)
print(10 < 9)

a = input("Enter first number")
b = input("Enter second number")
if a > b:
    print(f"The number {a} is greater than {b}")
else:
    print(f"The number {b} is greater than {a}")


print(bool("Hello"))
print(bool(0))
print(bool(1))
print(bool(["apple", "cherry", "banana"]))
"""


class myclass:
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


name = "Gaurav"
print("String Example:", name.upper())


is_student = True
print("Boolean Example:", is_student)


a, b = 10, 3
print("Operators Example: a+b=", a + b, " a*b=", a * b, " a/b=", a / b, " a%b=", a % b)


fruits = ["apple", "banana", "cherry"]
print("List Example:", fruits[0], "Length:", len(fruits))


colors = ("red", "green", "blue")
print("Tuple Example:", colors[1])


unique_numbers = {1, 2, 3, 2, 1}
print("Set Example:", unique_numbers)


person = {"name": "Rashmi", "age": 14}
print("Dictionary Example:", person["name"], "is", person["age"], "years old")


x = 20
if x > 18:
    print("If...Else Example: Eligible to vote")
else:
    print("If...Else Example: Not eligible")


day = 3
match day:
    case 1:
        print("Match Example: Monday")
    case 2:
        print("Match Example: Tuesday")
    case 3:
        print("Match Example: Wednesday")
    case _:
        print("Match Example: Other day")


count = 1
print("While Loop Example:")
while count <= 5:
    print("Count =", count)
    count += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
