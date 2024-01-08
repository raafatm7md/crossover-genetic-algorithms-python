import random


# Partially Matched Crossover
def pmx_crossover(parent1, parent2):
    # Select two random points within the length of the parents
    point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))

    # Create copies of the parents as the children
    child1, child2 = parent1.copy(), parent2.copy()

    # Initialize mapping dictionaries for swapping genes
    map1, map2 = {}, {}

    # Perform partially matched crossover between parents
    for i in range(point1, point2):
        child1[i], child2[i] = child2[i], child1[i]  # Swap genes between parents
        map1[child1[i]] = child2[i]  # Create mapping for child1 genes from parent2
        map2[child2[i]] = child1[i]  # Create mapping for child2 genes from parent1

    # Repair the rest of the chromosome using the created mapping
    for i in range(len(child1)):
        if i in range(point1, point2): continue
        while child1[i] in map1.keys():
            child1[i] = map1[child1[i]]
        while child2[i] in map2.keys():
            child2[i] = map2[child2[i]]

    # Return the resulting children after crossover and repair
    return child1, child2


# Another method for Partially Matched Crossover
def pmx2_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))

    child1, child2 = parent1.copy(), parent2.copy()

    map = {}

    # Perform partially matched crossover between parents
    for i in range(point1, point2):
        child1[i], child2[i] = child2[i], child1[i]  # Swap genes between parents

        if child2[i] in map.keys():  # If child2 gene already mapped
            map[child1[i]] = map[child2[i]]  # Map child1 gene to the same value as child2
            map.pop(child2[i])  # Remove child2 gene mapping
        elif child1[i] in map.values():  # If child1 gene value already used
            # Find the key associated with the child1 gene's value and map it to child2
            map[[k for k, v in map.items() if v == child1[i]][0]] = child2[i]
        else:
            map[child1[i]] = child2[i]

    # Repair the rest of the chromosome using the created mapping
    for i in range(len(child1)):
        if i in range(point1, point2): continue
        if child1[i] in map.keys():
            child1[i] = map[child1[i]]
        if child2[i] in map.values():
            child2[i] = [k for k, v in map.items() if v == child2[i]][0]

    return child1, child2