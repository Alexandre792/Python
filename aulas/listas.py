minha_lista = [1,2,3,4]
minha_lista[3] = 10 #mudando o valor 4 por 10 pelo indice
minha_lista.append(12)
minha_lista.remove(2) #remove o valor de fato
del minha_lista[0] #remove pelo o indice

for elemento in minha_lista: #percorre todo o indice um por um " nao esquecer o print elemento"
    print(minha_lista)

    x=5
    if x in minha_lista:
        print(f"o valor {x} estar na minha lista ")
                                                    
    else:     
        print(f"o valor {x} não estar na minha lista")


        minha_lista = [4,6,3,7,9,33]
        minha_lista.reverse() #colocar a lista em ordem reversa
        minha_lista.sort() #alinha a lista em ordem certa

        minha_lista.extend(minha_lista) #junta a lista com outra que vc quer criar
        

   
