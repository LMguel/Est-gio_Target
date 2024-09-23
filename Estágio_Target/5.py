def inverter_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida 
    return invertida

texto = "Exemplo de string"
print(f"String original: {texto}")
print(f"String invertida: {inverter_string(texto)}")
