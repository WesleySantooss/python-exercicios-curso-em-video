print ('-=' * 20)
print ('Analisador de Triângulos v2.0')
print ('-=' * 20)

lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))

tipotriangulo = ''

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        tipotriangulo = 'EQUILÁTERO'
    elif lado1 != lado2 != lado3 != lado1:
        tipotriangulo = 'ESCALENO'
    else:
        tipotriangulo = 'ISÓSCELES'
    print (f'Os segmentos acima PODEM FORMAR um triângulo {tipotriangulo}!')
else:
    print ('Os segmentos acima NÃO PODEM FORMAR um triângulo!')