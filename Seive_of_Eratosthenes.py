# Finds all prime numbers in a given range

print('The Seive of Eratosthenes will find all prime numbers in a given range')

def seive_of_e():
  limit = input('Input an integer for the upper limit: ')
  limit = int(limit) + 1

  sieve = [True] * (limit)
  output = []
  for i in range(2, int(limit)):
    if sieve[i]:
      output += [str(i)]
      for j in range(i*i, int(limit), i):
        sieve[j] = False
  print(f'Prime numbers: {output}')

seive_of_e()