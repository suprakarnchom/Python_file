def loop1():
    for i in range(11):
        print(i)

def loop2():
    for i in range(1, 11):
        print(i)

def loop_string():
    for c in 'i like python':
        print(c.upper())

def loop_tuple():
    flowers = "rose", "lily", "tulip", "daisy"
    for f in flowers:
        print(f.capitalize())

def loop_tuple2():
    flowers = "rose", "lily", "tulip", "daisy"
    for i in range(len(flowers)):
        print(i+1,flowers[i].capitalize(), sep=". ",)

def temperature_table():
    for celcius in range(101):
        f = (celcius*9/5) + 32
        print(celcius,"=", f)

def temperature_table2():
    for celcius in range(101):
        f = (celcius*9/5) + 32
        print("{}C = {:.2f}F".format(celcius, f))

def mult_table(from_n, to_n):
    for i in range(from_n, to_n +1):
        for j in range(1, 13): #nested loop
            print("{} x {} = {}".format(i, j, i*j))
        print("-"*20)

print(mult_table(2, 3))
