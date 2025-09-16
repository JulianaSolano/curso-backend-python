Cdef calculadora(x, y, n):

    if n == '1':
        result = x * y
    elif n == '2':
        result = x + y
    elif n == '3':
        result = x - y

    return result

# --- Código para interagir com o usuário ---
print("Escolha a operação:")
print("1 - Multiplicação")
print("2 - Adição")
print("3 - Subtração")

opcao = input("Qual opção deseja? (1, 2 ou 3): ")
n1 = float(input("Escreva o primeiro n°: "))
n2 = float(input("Escreva o segundo n°: "))

r = calculadora(n1, n2, opcao)
print("O resultado é:", r)
