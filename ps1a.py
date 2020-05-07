###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    file = open(filename, 'r')
    cows = {}
    for line in file:
        cow = line.split(',')
        cows[cow[0]] = int(cow[1])
    file.close()
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # Sorting cows by their weight
    sorted_cows = sorted(cows.items(), key=lambda item: item[1], reverse=True)

    sorted_cows_copy = sorted_cows.copy()
    transport_list = []

    while len(sorted_cows) > 0:
        current_transport = []
        total_weight = 0
        for cow in sorted_cows:
            if total_weight + cow[1] <= limit:
                current_transport.append(cow[0])
                total_weight += cow[1]
                sorted_cows_copy.remove(cow)
        transport_list.append(current_transport)
        sorted_cows = sorted_cows_copy.copy()

    return transport_list

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    for partition in get_partitions(cows.keys()):
        flag = True
        for item in partition:
            total_weight = 0
            for cow in item:
                total_weight += cows[cow]
            if total_weight > limit:
                flag = False
                break
        if flag:
            return partition

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass

cows = load_cows("ps1_cow_data_3.txt")
print("List of cows:\n",cows,'\n')

start = time.time()
greedy_transport = greedy_cow_transport(cows)
end = time.time()
print("Total number of transports with greedy:", len(greedy_transport), "trips. Calculated in", '%.6f'%(end-start),"sec")
print(greedy_transport)
print()

start = time.time()
brute_force_transport = brute_force_cow_transport(cows)
end = time.time()
print("Total number of transports with brute force:", len(brute_force_transport), "trips. Calculated in", '%.6f'%(end-start),"sec")
print(brute_force_transport)
print()