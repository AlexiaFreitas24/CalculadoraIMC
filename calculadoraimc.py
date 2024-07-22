print('Calculadora de Imc')

altura = input('Digite sua altura ')

altura_convert = float(altura)
altura_altura = altura_convert*altura_convert

peso = input('Digite seu peso ')

peso_convert = float(peso)
imc = peso_convert / altura_altura

print('Seu IMC é', imc)
