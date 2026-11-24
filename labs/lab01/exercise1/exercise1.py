def is_budget_sufficient(one_way_km, budget):
    fuel = (one_way_km / 5) * 2
    suffient = bool(fuel <= budget)
    return suffient

