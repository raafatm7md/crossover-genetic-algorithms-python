import random


# Order Crossover
def ox_crossover(parent1, parent2):
    # Determine the length of the parents
    length = len(parent1)

    # Select two points for crossover, ensuring they're in ascending order
    point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))

    # Create maps for the sections between the two points for both parents
    map1 = parent1[point2:] + parent1[:point2]
    map2 = parent2[point2:] + parent2[:point2]

    # Create child lists with None values to be filled
    child1, child2 = [None] * length, [None] * length

    # Perform crossover between the selected points
    for i in range(point1, point2):
        child1[i], child2[i] = parent2[i], parent1[i]
        map1.remove(child1[i])
        map2.remove(child2[i])

    # Fill the remaining elements in the children from the maps
    for i in range(point2, length):
        child1[i] = map1.pop(0)
        child2[i] = map2.pop(0)
    for i in range(0, point1):
        child1[i] = map1.pop(0)
        child2[i] = map2.pop(0)

    # Return the resulting children after crossover
    return child1, child2
