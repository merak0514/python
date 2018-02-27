# List Comprehension
# HIGH LIGHT
no_primes = [j for i in range(2, 10) for j in range(i * 2, 100, i)]
primes = [i for i in range(2, 100) if i not in no_primes]
print(primes)
