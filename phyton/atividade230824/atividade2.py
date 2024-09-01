# variavel global
contador= 0

#função para incrementar o contador
def incrementar_contador():
   global contador
   contador += 1
   mensagem = "o valor do contador é : " + str(contador)
   print(mensagem)

   # testando a função 
incrementar_contador()
# tentando imprimir a variável mensagem fora da função
print(mensagem)
   