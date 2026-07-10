numbers = [10, 25, 8, 45, 67, 45, 67, 30]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second Largest:", unique_numbers[-2])
else:
    print("Not enough unique elements.")
