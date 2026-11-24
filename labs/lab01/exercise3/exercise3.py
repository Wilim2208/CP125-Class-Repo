def validate_entry(name, pin):
    result = bool((name == "Director" and pin == 1122) or (name == "Security" and pin == 9900))
    return result