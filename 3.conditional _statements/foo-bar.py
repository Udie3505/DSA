num : int = int(input("enter number: "))

if num%3 == 0 and num%5 == 0:
    print("FOOBAR")
elif num%5 == 0:
    print("BAR")
elif num%3 == 0:
    print("FOO")
else:
    print("FOOFOOBARBAR")
