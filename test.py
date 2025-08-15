import math
import matplotlib.pyplot as plt

def P(a,b):
  if a == 0 or b == 0:
    return 0
  if b == 1:
    return a
  r = a % b
  q = (a-r)/b
  p = (b+1)*q*b/2 + P(b,r)
  return int(p)

def is_weak_triangular_prime(n):
  for i in range(2,int(2*n/3)+1):
    for k in range(2,i+1):
      if math.gcd(i,k) != 1:
        continue
      if n == P(i,k):
        return False

  return True


def is_triangular_prime(n):
  for i in range(2,int(2*n/3)+1):
    for k in range(2,i+1):
      if n == P(i,k):
        return False

  return True

from sympy import isprime
import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x/np.log(x)
N = 300
input  = np.linspace(0,N, 1)
output = f(input)
xs = np.arange(N+1)
primes = np.vectorize(isprime)(xs)
weak_primes = np.vectorize(is_weak_triangular_prime)(xs)

y1 = np.cumsum(primes)
y2 = np.cumsum(weak_primes)
# y2 = primes/output
ax = plt.subplot()
# ax.step(xs, y1, marker='o', where='post', label='primes')
ax.step(xs, y2, marker='o', where='post', label='weak primes')
ax.plot(input, output)
ax.set_yticks(xs)
ax.set_xticks(xs)

ax.legend()

#   if (i % 10000 == 0):
#     print(f"----------- {i} reached")
#   a = len(remainders_sequence)
#
#
#   if remainders[0:a] == remainders_sequence:
#     if is_prime(i):
#       sequence.add(greatest_in_sequence)
#       greatest_in_sequence = i
#       remainders_sequence = remainders
#       print("NEW ONE FOUND: " + str(greatest_in_sequence))
#       with open("sequence.txt", "a") as file:
#     # Write new content to the end of the file
#         file.write(f"{greatest_in_sequence},")
#
#
# print(list(sequence))

# a = math.sqrt(2*180253)
# remainders = []
# for k in range(1, int(a)+1):
#     remainders.append(int(180253%(k*(k+1)/2)))
#
plt.show()