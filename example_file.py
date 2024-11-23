# Exercise 3. Sum of all Digits 🔢

# You have a mixed string that contains both letters and numbers, like an alphanumeric password or
# a serial key. Your task is to find all the numbers in this string and sum them up.

# Hint: You can put the numbers you find into a list (cast as `int`) and use `sum()` on the list at the end.

mixed_string = "abc123xyz456"
digits = "0123456789"
found_digits = []

for char in mixed_string:
    if char in digits:
        found_digits.append(int(char))

print(f"The total sum of numbers in the string is: {sum(found_digits)}")
