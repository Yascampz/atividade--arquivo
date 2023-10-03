'''
Faça um codigo que leia N números inteiros e salve em um arquivo.

Abra o arquivo e imprima a média dos valores
'''

with open ('atividade.txt','w') as arquivo:
    continuar=True
    while continuar == True:
        x=int(input("Digite um número inteiro ou digite 00 para parar: "))
        if x==00:
            continuar=False
        else:
            arquivo.write(str(x)+'\n')

with open ('atividade.txt','r') as arquivo:
    i=0
    soma=0
    divisor=0
    for x in arquivo:
        soma=soma+int(x)
        divisor+=1
    media=soma/divisor
    print("a média dos numeros inseridos é "+str(media))