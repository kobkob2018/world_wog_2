def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
difficulty_levels = {
    '-1': {'name': 'None selected', 'multiplier': -1},
    '1': {'name': 'Just let me win...', 'multiplier': 1},
    '2': {'name': 'Easy', 'multiplier': 2},
    '3': {'name': 'Medium', 'multiplier': 3},
    '4': {'name': 'Hard', 'multiplier': 4},
    '5': {'name': 'Impossible', 'multiplier': 5}
}