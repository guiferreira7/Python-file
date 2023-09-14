moeda = True
ponto = 0
nome = str(input('Nome do Personagem:\n'))
if(((nome == "Mario" and moeda == True)or(nome == "mario" and moeda == True))):
    ponto = ponto + 1
    print(f'{nome} pegou a moeda e teve {ponto}')
    moeda = str(input("Deseja pegar mais uma moeda?\n"))
    if(moeda == "sim"):
        ponto = ponto + 1 
        print(f'{nome} pegou a moeda e teve {ponto}')
    else:
        print(f'Não quis pegar mais moedas')
else:
    print('Não pegou a moeda')    
