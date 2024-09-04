def count_a(string):
    count = string.lower().count('a')
    return count

# Testando com uma string específica
string = input("Informe uma string: ")
count = count_a(string)
print(f"A letra 'a' ocorre {count} vezes na string '{string}'.")