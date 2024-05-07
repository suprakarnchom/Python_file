def demo1():
    i = 1
    while i <= 10:
        print(i)
        i += 1 # i = i + 1
    print("Done")

def sum_input():
    n = int(input("Enter a number: "))
    total = 0
    while n != 0:
        total += n # total = total + n
        n = int(input("Enter a number: "))
    print("Total:", total)

def sum_input_repeat_until():
    total = 0
    while True:
        n = int(input("Enter a number: "))
        if n != 0:
            total += n # total = total + n
        else:
            break
    print("Total:", total)

sum_input_repeat_until()