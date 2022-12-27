titulo = 'MEDIA ARITMÉTICA'
print (f'{titulo:=^40}')

nota1= float (input('Qual a primeira nota '))
nota2= float (input('Qual a segunda nota '))
media = (nota1 + nota2) / 2

print (f'{media:.2f}')

if media < 5:
    print ('REPROVADO')
elif media > 5 and media < 6.9:
    print ('RECUPERAÇÃO')
elif media > 7 and media <=10:
    print ('APROVADO')
