"""
Qual será a saída depois de rodar o seguinte código? 
a = ["Monday", "Wednesday", "Thursday"] a.insert(1,"Tuesday") a.append("Friday") print(a)

A. ["Tuesday", "Monday", "Wednesday", "Thursday", "Friday"]
B. [ "Monday", "Tuesday, "Wednesday", "Thursday", "Friday"]
C. ["Monday", "Wednesday", "Thursday"]
D. ["Monday", "Wednesday", "Thursday"]

"""

a = ["Monday", "Wednesday", "Thursday"]

#o insert adiciona o valor específico, no lugar específico da lista
#logo o valor será adicionado após o "monday", cuja o valor é "0"

a.insert(1,"Tuesday")

#o append adiciona o valor ao final da lista
#ou seja, após o "Thursday"

a.append("Friday")
print(a)

"""
  output:
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        Process finished with exit code 0
        
"""
