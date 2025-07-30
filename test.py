import math
def triangulate(b):
    return b*(b+1)/2
def lattices(a,b):
    if b == 0:
        return 0
    if b == 1:
        return a
    r=a%b
    q = (a-r)//b
    p = triangulate(b)*q + lattices(b,r)
    return p

def is_prime(p):
  if p % 3 != 1:
    return False
  # print(max)
  for i in range(2, int(math.sqrt(2*p))+3):
    for k in range(2, math.ceil(2*p/(i+1))):

      value = lattices(k,i)
      if int(value) == int(p):
        return False

  return True

K_MAX = 2**32

sequence = set()
greatest_in_sequence = 4
remainders_sequence = [0, 1, 1]
for i in range(greatest_in_sequence,K_MAX):
  a = math.sqrt(2*i)
  remainders = []
  for k in range(1, int(a)+1):
    remainders.append(int(i%(k*(k+1)/2)))
  #print(f"{i}: {remainders} \n")
  if (i % 10000 == 0):
    print(f"----------- {i} reached")
  a = len(remainders_sequence)


  if remainders[0:a] == remainders_sequence:
    if is_prime(i):
      sequence.add(greatest_in_sequence)
      greatest_in_sequence = i
      remainders_sequence = remainders
      print("NEW ONE FOUND: " + str(greatest_in_sequence))
      with open("sequence.txt", "a") as file:
    # Write new content to the end of the file
        file.write(f"{greatest_in_sequence},")


print(list(sequence))

# a = math.sqrt(2*180253)
# remainders = []
# for k in range(1, int(a)+1):
#     remainders.append(int(180253%(k*(k+1)/2)))
#
# print(remainders)
