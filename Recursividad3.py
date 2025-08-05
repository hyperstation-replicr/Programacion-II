def is_prime(n, divisor=2):
  if n<2:
    return False
  if divisor * divisor > n:
    return True
  if n % divisor == 0:
    return False
  return is_prime(n, divisor + 1)
print (is_prime(7))
print (is_prime(9))
