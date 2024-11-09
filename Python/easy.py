import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Create set B with the first 1000 odd numbers
set_b = set(range(1, 2000, 2))

# Find the upper bound of set B
upper_bound = max(set_b)

# Create set A with prime numbers up to the upper bound of set B
set_a = set(num for num in range(2, upper_bound + 1) if is_prime(num))

# Find the intersection of set A and set B
intersection = set_a.intersection(set_b)

# Calculate P(A|B)
probability_a_given_b = len(intersection) / len(set_b)

# Print the results
print(f"Number of elements in set B (first 1000 odd numbers): {len(set_b)}")
print(f"Upper bound of set B: {upper_bound}")
print(f"Number of elements in set A (prime numbers up to {upper_bound}): {len(set_a)}")
print(f"Number of elements in the intersection (odd primes in set B): {len(intersection)}")
print(f"P(A|B) = {probability_a_given_b:.6f}")

# Print the intersection elements
print("\nIntersection elements (odd primes in set B):")
print(sorted(intersection))"# basic" 
