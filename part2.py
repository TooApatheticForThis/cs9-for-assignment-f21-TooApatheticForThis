"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""

number = int(input("enter the number you'd like to do this crazy operation to: "))
total = 0

for i in range(number + 1):
  total = total + i * i * i
  print(total)

print("")
print("and the winner is: ")
print(total)
