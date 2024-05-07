'''def divide_by(a, b):
        return a / b
try:
    ans = divide_by(10, 0)
except ZeroDivisionError as e:
    print(e,"We cannot divide by zero")
except Exception as e:
    print(e,"Something went wrong")'''

# Starter code
'''def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "We cannot divide by zero")'''

'''try:
    items = [1,2,3,4,5]
    item = items[6]
    print(item)
except IndexError as e:
    print(e,"Index out of range")
except Exception as e:
    print(e,"Something went wrong")'''

# Starter code

try:
    open('file_does_not_exist.txt', 'r') 
except FileNotFoundError as e:
    print("The file could not be found")
     

