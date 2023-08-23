def find_prime (primes):
        i = 1
        primes[0] = 0
        while (i * i <= 620000):
            if (primes[i] == 1):
                j = i + i + 1
                while (j < 620000):
                    primes[j] = 0
                    j = j + i + 1
            i = i + 1

a,b,c = str (input ()).split ()
a = int (a)
b = int (b)
c = int (c)

primes = [1] * 620000 

find_prime (primes)

person_index = c - 1
d = 0
prime_index = 0

primes2 = []

while (d < b):
    prime_index = primes.index (1, prime_index) + 1
    prime_number = prime_index
    primes2.append (prime_number)

    prime_number = prime_number % (a * (a - 1))
    cycles = prime_number // a
    moves = prime_number % a

    if (person_index > 0):
        person_index = person_index - cycles
        
        if (person_index < 1):
            person_index = -((-person_index) % (a - 1)) + a - 1
            
        if (person_index <= moves):
            person_index = person_index - 1

    else:
        person_index = person_index + moves
    
    d = d + 1

person1_index = person_index + 1
person2_index = person_index - 1

if (person1_index > a - 1):
    person1_index = 0

if (person2_index < 0):
    person2_index = a - 1

while (b > 0):
    prime_number = primes2[b - 1] % (a * (a - 1))
    cycles = prime_number // a
    moves = prime_number % a

    if (person1_index < moves):
        person1_index = person1_index + 1
    elif (person1_index == moves):
        person1_index = 0
    
    if (person1_index > 0):
        person1_index = person1_index + cycles
    
        if (person1_index > a - 1):
            person1_index = person1_index % (a - 1)

    if (person2_index < moves):
        person2_index = person2_index + 1
    elif (person2_index == moves):
        person2_index = 0
    
    if (person2_index > 0):
        person2_index = person2_index + cycles
    
        if (person2_index > a - 1):
            person2_index = person2_index % (a - 1)
    
    b = b - 1

print (person1_index + 1, person2_index + 1)