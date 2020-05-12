###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    def get_density(list_of_weights):
        if list_of_weights == None:
            return 0
        elif len(list_of_weights) == 0:
            return 0
        else:
            return sum(list_of_weights)/len(list_of_weights)

    try:
        result = memo[(len(egg_weights), target_weight)]
    except KeyError:
        if egg_weights == () or target_weight == 0:
            # Using tuple, instead of list, for storing the results with eliminate the danger of mutation
            result = ()
        elif egg_weights[-1] > target_weight:
            result = dp_make_weight(egg_weights[:-1], target_weight, memo)
        else:
            nextEggWeight = egg_weights[-1]
            # Explore the left branch
            withToTake = dp_make_weight(egg_weights, target_weight - nextEggWeight, memo)
            density_withToTake = get_density(withToTake + (nextEggWeight,))
            # Exploring the right branch
            withoutToTake = dp_make_weight(egg_weights[:-1], target_weight, memo)
            density_withoutToTake = get_density(withoutToTake)

            if density_withToTake > density_withoutToTake:
                result = withToTake + (nextEggWeight,)
            else:
                result = withoutToTake
        memo[(len(egg_weights), target_weight)] = result
    return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    actual_output = dp_make_weight(egg_weights, n)
    print("Actual output:", len(actual_output), actual_output)


