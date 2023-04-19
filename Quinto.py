def inverter_string(string):
   
    lista_caracteres = list(string)
    
    inicio = 0
    fim = len(lista_caracteres) - 1

    
    while inicio < fim:
        
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        
        inicio += 1
    
        fim -= 1

    
    return "".join(lista_caracteres)



string = "Bom dia!"
string_invertida = inverter_string(string)

print("String original:", string)
print("String invertida:", string_invertida)

