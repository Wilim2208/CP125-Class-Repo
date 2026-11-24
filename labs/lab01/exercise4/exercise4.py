def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electirc":
        price = hour * 2
    elif vehicle_type == "Hybrid":
        if hour >-1 and hour < 6 and hour >= 22 and hour < 24:
            price = hour * 2
        else:
            price = hour 5
    else:
        price = hour * 5
    return price