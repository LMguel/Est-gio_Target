def pertence_fibonacci(num):
    a, b = 0, 1
    fibonacci_sequence = [a, b]  # Lista para armazenar a sequência

    while b <= num:
        fibonacci_sequence.append(b)
        a, b = b, a + b

    if num in fibonacci_sequence:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."

# Número informado previamente
numero = 21  # Você pode alterar esse valor para testar outros números
resultado = pertence_fibonacci(numero)
print(resultado)
