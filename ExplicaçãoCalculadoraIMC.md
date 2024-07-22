altura = input('Digite o sua altura ') 
#Recebe a altura do usuário
altura_convert = float(altura) 
#Converte o valor de texto em float
altura_altura = altura_convert * altura_convert 
#Realiza a primeira conta e armazena na variável altura_altura

peso = input('Digite o seu peso ') 
#Recebe o peso do usuário
peso_convert = float(peso) 
#Converte o valor de texto em float
imc = peso_convert / altura_altura  
print(imc) 
#Retorna o resultado da conta do IMC
