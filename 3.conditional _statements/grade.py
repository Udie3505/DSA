num :int = int(input("enter num of marks: "))

if 91 <= num <= 100:
    print("A")
elif 81 <= num <= 90:
    print("B")
elif 71 <= num <= 80:
    print("c")
elif 61 <= num <= 70:
    print("D")
elif 1 <= num <= 60:
    print("fail")
else:
    print("Invalid input")