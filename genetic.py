import random

def fitness(individual):
    return sum(individual) #generate code

def select(population, fitnesses):
    return random.choices(population, weights=fitnesses, k=2)

def crossover(p1, p2):
    point = random.randint(1, len(p1)-1)
    return p1[:point] + p2[point:], p2[:point] + p1[point:]

def mutate(individual, mutation_rate=0.1):
    return [1-gene if random.random() < mutation_rate else gene for gene in individual]

population = [[random.randint(0,1) for _ in range(8)] for _ in range(10)]
for gen in range(50):
    fitnesses = [fitness(ind) for ind in population]
    new_population = []
    for _ in range(len(population)//2):
        p1, p2 = select(population, fitnesses)
        c1, c2 = crossover(p1, p2)
        c1, c2 = mutate(c1), mutate(c2)
        new_population.extend([c1, c2])
    population = new_population
best = max(population, key=fitness)
print("Best individual:", best, "Fitness:", fitness(best))