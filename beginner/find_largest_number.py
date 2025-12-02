

def largest_number(numbers: list,last_number_position: int):
    return list(sorted(numbers,reverse=True))[:int(last_number_position)]


print(largest_number([9,8,3,4,4,2,7],4))