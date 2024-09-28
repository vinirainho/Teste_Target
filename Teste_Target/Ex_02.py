def sequenciaFibonacci(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci

def procurarNumero(n):
    sequencia = sequenciaFibonacci(n)

    if n in sequencia:
        return f"O número {n} está na sequência de Fibonacci."
    else:
        return f"O número {n} não está na sequência de Fibonacci."
numero = int(input("Digite o número: "))
resultado = procurarNumero(numero)
print(resultado)


    