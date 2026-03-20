m = float(input('Uma distância em metros: '))
print ('A medida de {}m corresponde a'.format(m))
print ('{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format((m / 1000), (m / 100), (m / 10), (m * 10), (m * 100), (m * 1000)))

m = float(input('Uma distância em metros: '))
print ('A medida de {}m corresponde a'.format(m))
print (f'{m / 1000}km \n{m / 100}hm \n{m / 10}dam \n{m * 10:.0f}dm \n{m * 100:.0f}cm \n{m * 1000:.0f}mm')