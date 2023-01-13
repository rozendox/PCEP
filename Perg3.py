"""
Qual será a saída depois de rodar o seguinte código? def fun(data, *num ): print(data) fun("Earth", 2,
True, "Jupiter")

A. Earth
B. Earth Jupiter
c. 2
D. 2 True

"""


#função fun, que recebe os parâmetros data, e num
def fun(data, *num ):
    #imprime os valores nos parâmetros
    print(data)

fun("Earth", 2,True, "Jupiter")

"""
  output:
        Earth
"""        
