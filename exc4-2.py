import math
number = (int(input(f'Digite o numero desejado:')))
if(number == 0):
    print(f'O {number} é nulo')    

elif(number % 2 == 0):
    print(f'O {number} é par')
else:
    print(f'O {number} é impar')