# Three Parents Crossover
def three_parents_crossover(parent1, parent2, parent3):
    # Initializing an empty list to store the child
    child = []

    # Looping through each index of the parents
    for i in range(len(parent1)):
        # If the elements at the same index in parent1 and parent2 are equal,
        # add that element to the child
        if parent1[i] == parent2[i]:
            child.append(parent1[i])
        # If the elements at the same index in parent1 and parent2 are not equal,
        # add the element from parent3 to the child
        else:
            child.append(parent3[i])

    # Returning the resulting child after crossover
    return child