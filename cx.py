# Cycle Crossover
def cx_crossover(parent1, parent2):
    # Create a dictionary to track the mappings between elements of parent1 and parent2
    map, i = {}, 0

    # Establish the first mapping between the elements of parent1 and parent2
    map[parent1[i]] = parent2[i]

    # Continue mapping until the cycle is complete or there's a break in the cycle
    while map[parent1[i]] in parent1:
        if map[parent1[i]] in map.keys():  # Check for breaks in the cycle
            break
        i = parent1.index(map[parent1[i]])  # Move to the next element in the cycle
        map[parent1[i]] = parent2[i]  # Map the corresponding elements

    length = len(parent1)
    # Initialize child1 and child2 as lists of 'None' values
    child1, child2 = [None] * length, [None] * length

    # Create two child sequences based on the mapping information
    for i in range(length):
        if parent1[i] in map.keys() and parent2[i] is map[parent1[i]]:
            # If the element in parent1 has a mapping in the dictionary, assign the elements accordingly
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        else:
            # If no mapping exists, swap the elements between child1 and child2
            child1[i] = parent2[i]
            child2[i] = parent1[i]

    return child1, child2  # Return the two generated child sequences
