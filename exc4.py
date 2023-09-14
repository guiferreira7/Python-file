import math
from datetime import date
p = 1
diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year
diaNascimento = int(input('Dia do Nascimento: '))
mesNascimento = int(input('Mes de seu nascimento: '))
anoNascimento = int(input('Ano que voçê nasceu: '))
print(f'{diaAtual}/{mesAtual}/{anoAtual}')
r = anoAtual - anoNascimento


if(mesNascimento > mesAtual):
    r = (anoAtual - anoNascimento) - p
    
    print(r)

if (mesNascimento == mesAtual and diaNascimento < diaAtual):
    y = anoAtual - anoNascimento   
    
    print(y)

if(diaAtual == diaNascimento and mesAtual == mesNascimento):
    g = anoAtual - anoNascimento
    print(g)

elif(diaAtual < diaNascimento and mesAtual == mesNascimento):
    u = anoAtual - anoNascimento - p
    print(u)

else:
    h = anoAtual - anoNascimento 
    print(h)

if(diaAtual == diaNascimento and mesAtual < mesNascimento):
    d = anoAtual - anoNascimento
    print(d)
