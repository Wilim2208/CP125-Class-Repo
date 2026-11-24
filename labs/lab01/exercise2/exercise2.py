
import math
def calculate_tent_cost(participants, tent_capacity, tent_price):
    cost = math.ceil(participants / tent_capacity) * tent_price
    return cost

