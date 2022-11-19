

def mean(numbers):
    total = sum(numbers)
    length = len(numbers)
    return total / length

def difference(numbers):
    first = numbers[0]
    rest = numbers[1:]
    return first - sum(rest)