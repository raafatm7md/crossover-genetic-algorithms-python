import random


# Single Point Crossover
def single_point_crossover(parent1, parent2):
    # Determine a random point for crossover within the length of the parents
    crossover_point = random.randint(1, len(parent1) - 1)

    # Create children by swapping genetic material at the crossover point
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Two-Points Crossover
def two_points_crossover(parent1, parent2):
    # Select two random crossover points and sort them
    crossover_point1, crossover_point2 = sorted(random.sample(range(1, len(parent1)), 2))

    # Create children by swapping genetic material between the two points
    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
    return child1, child2


# Multi-Points Crossover
def multi_points_crossover(parent1, parent2, num_points=None):
    # If the number of crossover points is not specified, select a random number
    if num_points is None:
        num_points = random.randint(1, len(parent1))

    # Select random crossover points and sort them
    points = sorted(random.sample(range(1, len(parent1)), num_points))

    # Initialize children
    child1 = []
    child2 = []
    i = 0

    # Iterate through the crossover points
    for i in range(num_points):
        if i == 0:
            child1 += parent1[:points[i]]
            child2 += parent2[:points[i]]
            continue
        if i % 2 == 0:
            child1 += parent1[points[i - 1]:points[i]]
            child2 += parent2[points[i - 1]:points[i]]
        else:
            child1 += parent2[points[i - 1]:points[i]]
            child2 += parent1[points[i - 1]:points[i]]

    # Combine remaining genetic material after the last crossover point
    if i % 2 == 0:
        child1 += parent2[points[i - 1]:]
        child2 += parent1[points[i - 1]:]
    else:
        child1 += parent1[points[i - 1]:]
        child2 += parent2[points[i - 1]:]

    return child1, child2
