# Série de Fibonacci
# Posição (n): 0      1       2       3       4       5       6
# Termo (fib): 0      1       1       2       3       5       8

def fibonacci_i(n):
    fib = 0
    k = 1    
    for i in range (0, n, 1):
        j = fib + k
        fib = k 
        k = j
    return fib

def fibonacci_r(n):
    if n < 2:
        return n 
    else:
        return fibonacci_r(n-1) + fibonacci_r(n-2)
    
entrada = 2
    
resultado = fibonacci_i(entrada)
print("Resultado de fibonacci_i(): ", resultado)

resultado = fibonacci_r(entrada)
print("Resultado de fibonacci_r(): ", resultado)

