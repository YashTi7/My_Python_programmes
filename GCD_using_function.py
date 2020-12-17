def gcd(a,b):
  global af
  global bf
  af = []
  bf = []
  for i in range(1, a + 1):
    if a % i == 0:
      af.append(i)
    else:
      pass
  for i in range(1, b + 1):
    if b % i == 0:
      bf.append(i)
    else:
      pass
  while (1):
    global c
    c = bf[-1]
    if c in af:
      print(c, ' is the HCF')
      break
    else:
      bf.remove(c)


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

gcd(a,b)
