#Python Coding Test

import random

# Define function that takes a list of values and a list of weights for each value
# Returns a value from values list with a probability based on the weight assigned to it. 

def weighted_random(values, weights):
    total_weight = sum(weights)
    acum_weights = [w / total_weight for w in weights[:]] # Make weights probabilities
    rand = random.random() # Generate a random number from (0,1) uniform distribution
    for i in range(len(weights)-1):
        acum_weights[i+1] += acum_weights[i] # Make cummulative probabilities
    for value, weight in zip(values, acum_weights):
        if weight > rand:
            return value # Return the first value from the list that has cummulative probability greater than rand
