def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if n % i == 0: 
      is_prime = False
  if is_prime == True: 
    print("El número es primo. ")
  else: 
    print("El número no es primo. ")

n = int(input("Check this number: "))
prime_checker(n)