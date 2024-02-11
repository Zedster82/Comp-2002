

def sequence(iterations):
    a = 0
    b = 1
    c = a + b
    for i in range(iterations):
        print(a)
        a = b
        b = c
        c = b + a
    

sequence(50)