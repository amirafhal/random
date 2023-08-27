import random
value = random.randint(10,20)
c = 0
while c < 5:
  user = int(input("enter your value: "))
  if user == value:
    print(f"You win after {c} chances and the value is {value}")
    break
  else:
    c+=1
    if user > value:
      print("The value random is less than your value")
    else:
      print("The value random is greater than you value")
