#Ödev 1 Soru 1

l = list(range(1,11))
l[0:5], l[5:11] = l[5:11], l[0:5]
print(l)

#Ödev 1 Soru 2
n = int(input("Please enter a digit number: "))

if n >= 10:
  print(n, "is not a digit number. Please enter a digit number!")
else:
  for i in range(n):
    i = i + 1
    print(i)
