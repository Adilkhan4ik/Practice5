x = 10  # global variable

def change_global():
    global x
    x = 20

print(x)   # 10
change_global()
print(x)   # 20


def outer():
    y = 5   # enclosing variable
    
    def inner():
        nonlocal y
        y += 10
    inner()
    print(y)

outer()  # 15


a = 100  # global

def func():
    a = 50  # local
    print("Inside:", a)

func()          # Inside: 50
print("Outside:", a)  # Outside: 100


x = 1

def outer():
    y = 2
    
    def inner():
        global x
        nonlocal y
        x += 5
        y += 5
        print("Inner:", x, y)  # 6 7
    
    inner()
    print("Outer:", x, y) # 6 7

outer()
print("Global x:", x)  #6