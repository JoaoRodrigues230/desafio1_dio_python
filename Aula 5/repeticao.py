texto = input("DIGITE UMA PALAVRA: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print("\nFim do laço")
    
#tabuada

n = int(input("DIGITE UM NÚMERO: "))

print(f"TABUADA DO {n}:\n")

for p in range(n, (n*10)+1, n):
    
    print(p, end=" ")