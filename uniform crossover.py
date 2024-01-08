import random


# Uniform Crossover
def uniform_crossover(parent1, parent2):
    # Generate a mask to determine which genes come from which parent
    mask = [random.randint(0, 1) for _ in range(len(parent1))]

    # Initialize children as empty lists
    child1 = []
    child2 = []

    i = 0  # Initialize index to track gene position

    # Loop through the mask to perform crossover
    for gene in mask:
        if gene == 1:  # If the mask value is 1, keep the genes from the parents as they are
            child1.append(parent1[i])
            child2.append(parent2[i])
            i += 1  # Move to the next gene position
        else:  # If the mask value is 0, swap genes between parents
            child2.append(parent1[i])
            child1.append(parent2[i])
            i += 1

    # Return the resulting children after crossover
    return child1, child2