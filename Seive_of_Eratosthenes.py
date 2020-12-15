#Eratosthenes => pronounced 'air-uh-TAWS-thuh-neez'
print('The Seive of Eratosthenes will find all prime numbers in a given range; 0 and 1 are not primes.')

def seive_of_e(limit):
    limit = int(limit) + 1

    sieve = [True] * (limit)
    output = []
    for i in range(2, int(limit)):
        if sieve[i]:
            output += [i]
        for j in range(i*i, int(limit), i):
            sieve[j] = False
    print(f'Prime numbers: {output}')

limit = input('Input an integer for the upper limit: ')
seive_of_e(limit)