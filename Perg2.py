"""
Qual será a saída do código abaixo? x = 30 def change_me(): global x x += 30 print(30 + x)
change_me() print(x)

A. 60 90
B. 90 60
c. 90
D. 60


"""

#atribuindo a variavel x o valor de 30
x = 30

#função change me
def change_me():
    global x
    
    #x é igual a 30 + 30
    x += 30
    
    #imprime o valor de x (60) + 30, logo o valor vai ser 90
    
    print(30 + x)

#chama a função sem parâmetro    
change_me()

#imprime o valor somente de x
print(x)



"""
    output:
    
    90
    60
"""
