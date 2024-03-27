from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,3):
    nome = str(input('Digite seu nome: '))
    nasc = int(input('Em que ano {} você nasceu?: '.format(pess)))
    idade = atual - nasc
    print('Essa pessoa tem {} anos '.format(idade))
    if idade >=21:
        totmaior +=1
    else:
        totmenor+=1

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
