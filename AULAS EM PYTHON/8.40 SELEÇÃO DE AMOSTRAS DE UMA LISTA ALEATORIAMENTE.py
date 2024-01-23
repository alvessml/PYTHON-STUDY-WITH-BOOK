import random

print(random.sample(range(1, 101), 6))

a = list(range(1, 11))
random.shuffle(a)
print(a)