list = [10,15, 3, 4, 10, 10]
def count_even(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += 1
    return total

result = count_even(list)
print(result)
            
