peso = float(input('Qual é o seu peso?: (Kg)'))
altura = float(input('Qual é a sua altura ?: (m)'))
imc= peso /(altura**2)
print('O IMC é de {:.1f}.'.format(imc))

if imc <18.5:
    print('ABAIXO DO PESO')
elif 18.5 <=imc<25 :
    print('IDEAL')
elif 25<=imc<30:
    print('Sobrepeso')
elif 30<=imc<40:
    print('Obesidade')
elif imc>=40:
    print('Obesidade Mórbida')
    
    
