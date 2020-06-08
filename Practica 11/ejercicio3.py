#Estrategia bottom-up o programacion dinámica


def  fibonacci(numero):
    a = 1
    b = 1
    c = 0
    for i in range (1, numero-1):
        c = a + b
        a = b
        b = c
    return c


def  fibonacci2(numero):
    a = 1
    b = 1
    for i in range (1, numero-1):
        a,b = b, a+b
    return b

def fibonacci_bottom_up(numero):
    fib_parcial = [1, 1, 2]
    while len(fib_parcial) < numero:
        fib_parcial.append(fib_parcial[-1]+fib_parcial[-2])
        print(fib_parcial)
    return fib_parcial[numero-1]


f = fibonacci(10)
f2 = fibonacci2(10)
f3 = fibonacci_bottom_up(10)

print(f)
print(f2)
