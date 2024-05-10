my_list = [1, 2, 3]

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

# Test the function
print(factorial(5))  # Output: 120