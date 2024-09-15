# metodo 1
def saudação():
    print (f"ola mundo.")

saudação()    

#metodos 2
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(f"numero fatorial: {fatorial(5)}")


#metodo 3
nome = input("Informe seu nome: ")
idade = int (input("Informe sua idade: "))

if idade >= 18:
    print(f"maior de idade: {idade}")
else:
    print(f"menor de idade: {idade}")

#metodo 4
pessoa = {"nome": "Alexandre", "idade":32}

for chave, valor in pessoa.items()
    print(f"chave") #incompleto



   # metodo 5
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2==0:
        continue
    if numero == 7:
        break
    print(numero)

#metodo 5 
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2==0:
        print(f"numero par")
    else: 
         print(f"numero impar")


 #metodo 6

contador = 0

while(contador <= 5):
    print(f"Contador: {contador}")




