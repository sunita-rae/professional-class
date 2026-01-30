import random
import math
import matplotlib.pyplot as plt

city_names = ["A","B","C","D","E","F","G","H"]

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def path_length(path, cities):
    return sum(distance(cities[path[i]], cities[path[(i + 1) % len(path)]]) for i in range(len(path)))

def tsp(cities, iterations=5000):
    n = len(cities)
    best_path = list(range(n))
    random.shuffle(best_path)
    best_length = path_length(best_path, cities)

    for _ in range(iterations):
        new_path = best_path[:]
        i, j = random.sample(range(n), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        new_length = path_length(new_path, cities)

        if new_length < best_length:
            best_path, best_length = new_path, new_length

    return best_path, best_length

cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(8)]
path, length = tsp(cities)

x = [cities[i][0] for i in path] + [cities[path[0]][0]]
y = [cities[i][1] for i in path] + [cities[path[0]][1]]

plt.figure()
plt.scatter([c[0] for c in cities], [c[1] for c in cities])

for i, (x_city, y_city) in enumerate(cities):
    plt.text(x_city + 1, y_city + 1, city_names[i])

plt.plot(x, y)
plt.title(f"TSP Path with City Names - Distance: {length:.2f}")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

print("Best Path:", path)
print("Distance:", length)