import random

for i in range(5):
    print sorted(random.sample(range(1, 70), 5)),
    print random.choice(range(1, 27))
