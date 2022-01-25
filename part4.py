firstnumber = int(input("Enter a number: "))

for i in range(firstnumber + 1):
  if i % 3 == 0 and i % 5 == 0:
    print("fizzbuzz")
  elif i % 3 == 0:
    print("fizz")
  elif i % 5 == 0:
    print("buz z")
  else:
    print(i)

