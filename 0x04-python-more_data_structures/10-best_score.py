#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    
    max_score = float('-inf')
    best_key = None
    
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_key = key
    
    return best_key
