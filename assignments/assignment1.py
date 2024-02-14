##q1
# a = 5
# b = 10

# print(a > 5 and b >= 10) #f and t is f
# print(a >= 5 or not b > 10) #t or t is t 
# print(not ( a > 5 and b > 5)) #f and t not(f) is true
# print(not ( a < 10 or not b < 10)) #t or t is not(t) is f
# print(not ( not a <= 5 or not b >= 10)) #t or f is t 

#q2. converting kilometers to miles

# kilometers = float(input("enter the number of kilometers to convert into miles : "))
# miles = (kilometers*0.62137)
# print(f"{kilometers} kilometers in miles is: {miles} miles.")

#Q3 Ask 3 numbers from User and Calculate the Average.
# num1 = float(input("enter your number 1: "))
# num2 = float(input("enter your number 2: "))
# num3 = float(input("enter your number 3: "))
# average = ((num1+num2+num3)/3)
# print(f"average of {num1},{num2} and {num3} is : {average}")
# print(f"average = {average:.2f}")

#Q4) Ask value in Rupees and Convert into Paise
# value = float(input("enter the number of rupees: "))
# paise = value*100
# print(f"{value}rs is equal to {paise}paise.")

#Q5)Calculate Area of Square by taking side from User
# side = float(input("enter the side of square: "))
# area = side**2
# print(f"Area of square with side {side} is {area:.2f}")

#Q6) Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)
played = int(input("enter the number of games played: "))
won = int(input("enter the number of games won : "))
loss = int(input("enter the number of games lost: "))
if won + loss <= played:
    tied = (played-won-loss)
    total_points = (won*4 + tied*2)
    print(f"number of games tied : {tied}")
    print(f"Total points for {played} games is :{total_points} points.")
else:
    print(f"Invalid input. The sum of games won and games lost canoot exceed {played}")


#Q7)Check if the number entered by User is divisible by 3 or not.
# num = int(input("enter the number : "))
# if num%3 == 0:
#     print(f"{num} is divisible by 3")
# else:
#     print(f"{num}not divisible by 3")

#Q8)Ask a number from user. Print if the number is ODD or EVEN.
# num = int(input("enter the number : "))
# if num%2 == 0:
#     print(f"{num} is a even number")
# else:
#     print(f"{num} is a odd number")
#Q9. Take values of length and breadth of a rectangle from user and check if
#it is square or not.
# length = float(input("enter the length of the rectangle: "))
# breadth = float(input("enter the breadth of the rectangle: "))
# if length == breadth:
#     print(f"It is a Square")
# else:
#     print(f"It's not a square")
