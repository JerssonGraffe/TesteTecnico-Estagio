# String de entrada (pode ser alterada ou receber entrada do usuário)
string = input("Digite uma string: ")

# Inicializa uma variável para armazenar a string invertida
string_invertida = ""

# Itera sobre a string original de trás para frente
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Exibe a string invertida
print(f"String original: {string}")
print(f"String invertida: {string_invertida}")