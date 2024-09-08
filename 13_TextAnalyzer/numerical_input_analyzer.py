def total_numbers(number_list):
    return len(number_list)


def sum_of_numbers(number_list):
    return sum(number_list)


def range_of_numbers(number_list):
    return max(number_list) - min(number_list)


def frequency_numbers(number_list):
    frequency = {}
    for n in number_list:
        if n not in frequency:
            frequency[n] = 1
        else:
            frequency[n] += 1

    most_frequency = max(frequency, key=frequency.get)
    return most_frequency


def avg_numbers(number_list):
    if len(number_list) > 0:
        return sum_of_numbers(number_list) / len(number_list)


numbers_input = input("Enter a series of number separated by spaces:\n")

numbers_list = [int(num) for num in numbers_input.split() if num]


print("Number Analysis Results:")
print("-" * 23)
print("Total Numbers: ", total_numbers(numbers_list))
print("Sum of Numbers: ", sum_of_numbers(numbers_list))
print("Range of Numbers: ", range_of_numbers(numbers_list))
print("Most Frequent Numbers: ", frequency_numbers(numbers_list))
print("Average Numbers: ", avg_numbers(numbers_list))
