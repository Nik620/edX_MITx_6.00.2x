"""
    Solutions by Nik
"""

###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

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

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
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
    
    # create a useable list for analysis, as we don't know the names
    cows_sorted = sorted(cows.items(), key = lambda x: x[1], reverse = True)
    trips = []
    cows_taken = []
    
    #sort through the cows to see which is taken
    while len(cows_taken) < len(cows_sorted):
        trip_weight = 0
        trip = []
        for cow in cows_sorted: # noted issues in using tuple, trying as list
            cow = list(cow)
            if cow not in cows_taken: # checking if in list of taken
                if trip_weight + cow[1] <= limit:
                    trip_weight += cow[1] # adding cows weight
                    cows_taken.append(cow)
                    trip.append(cow[0])
        trips.append(trip)
        
    #return function
    return trips

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
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
    
    # now don't need a sorted list, running through cows
    cows_dict = cows.copy()
    cow_names = list(cows)
    valid_trips = []
    shortest_trips = [] 
    
    # loop to collect valid partitioned possibilities
    for trips in get_partitions(cow_names): # breaking into partitions
        valid_trip = [] # bool will check if any invalid partitions
        for trip in trips: # breaking partitions into ships
            trip_weight = 0 # reset weight
            for cow in trip: # individual cow in ship, assess wt
                trip_weight += cows_dict[cow] # calc wt
            if trip_weight <= limit: # wt limit check, true if <lim
                valid_trip.append(True)
            else:
                valid_trip.append(False)
        if False not in valid_trip: # checking to make sure no trips over 10
            valid_trips.append(trips)
    
    # loop over the valid_trips to find fewest
    for trips in valid_trips:
        if len(shortest_trips) == 0:
            shortest_trips = trips
        elif len(trips) < len(shortest_trips):
            shortest_trips = trips
    
    # return shortest trip
    return shortest_trips

        
# Problem 3
def compare_cow_transport_algorithms(cows, limit):
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
    # check for greedy time
    greedy_start = time.time()
    greedy_cow_transport(cows, limit)
    greedy_end = time.time()
    greedy_time = greedy_end - greedy_start
    
    # check for brute force time
    brute_force_start = time.time()
    brute_force_cow_transport(cows, limit)
    brute_force_end = time.time()
    brute_force_time = brute_force_end - brute_force_start
    
    print("Greedy time:", greedy_time)
    print("Brute Force time:", brute_force_time)
    
    return None


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms(cows, limit)


