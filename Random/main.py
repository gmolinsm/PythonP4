import random

for i in range (0,3):
    x = random.random()
    print(x)

for j in range (0,5):
    y = random.randint(0,100)
    print(y)

names = ["Jon", "Ana", "Maria", "Jim", "Florence", "George"]
print(random.choice(names))
