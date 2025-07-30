import sqlite3

def sequences():
    # TODO: actually retrieve from a databse
    return ["Fibonacci", "Catalan", "Binomial"]

def objects_by_sequence(sequence):
    # TODO: Return list of objects from DB associated with given sequence
    match sequence:
        case "Fibonacci":
            return []
        case "Catalan":
            return []
        case "Binomial":
            return []
        case _:
            return "Failed to find Sequence"
