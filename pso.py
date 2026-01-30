import random

def fitness(x):
    return x**2 + 4*x + 4

n = 5
positions = [random.uniform(-10, 10) for _ in range(n)]
velocities = [0]*n
pbest = positions[:]
gbest = min(pbest, key=fitness)

w, c1, c2 = 1, 2, 3

for _ in range(20):
    for i in range(n):
        r1, r2 = random.random(), random.random()
        velocities[i] = (w*velocities[i] +
                         c1*r1*(pbest[i]-positions[i]) +
                         c2*r2*(gbest-positions[i]))
        positions[i] += velocities[i]

        if fitness(positions[i]) < fitness(pbest[i]):
            pbest[i] = positions[i]

    gbest = min(pbest, key=fitness)

print("Best Value:", gbest)
print("Minimum Fitness:", fitness(gbest))