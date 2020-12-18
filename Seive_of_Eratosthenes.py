#Eratosthenes => pronounced 'air-uh-TAWS-thuh-neez'

print('The Seive of Eratosthenes will find all prime numbers in a given range; 0 and 1 are not primes.')

def seive_of_e(limit):
    limit = int(limit) + 1

    sieve = [True] * (limit)
    output = []
    total = 0
    for i in range(2, limit):
        if sieve[i]:
            output += [i]
            total += 1
        for j in range(i*i, limit, i):
            sieve[j] = False
    print("There are {} primes in {}.".format(total, limit-1))
    print(f'Prime numbers: {output}')


limit = input('Input an integer for the upper limit: ')
seive_of_e(limit)