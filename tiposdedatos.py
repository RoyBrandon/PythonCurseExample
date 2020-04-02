print('Hola mundo')

#comentarios xd

entero = 12
flotantes = 2.1212
strings = 'asdadsads'
booleano = True


suma =  2 + 4
resta = 6 - 3
multiplicacion = 5 * 3
division = 10 / 2
division_exacta = 5 // 2
modulo = 10 % 2

#print('El valor de la suma es:', suma)

#E mas solo deja concatenar con texto
#El float es un metodo

print('ingresa los numeros a sumar')

#Codigo para una suma de flotante con fornato a 2 decimales

numero_1 = float (input('ingresa el primer valor'))

numero_2 = float (input ('Ingresa el segundo valor'))

total = numero_1 + numero_2
print('El resultado es: ', '{:0.2f}'.format(total))

#Ejercicio de multiplicacion de flotantes a 3 decimales 

n_1 = float (input('infrasa primer numero: '))
n_2 = float (input ('ingresa segundo numero: '))

mult = n_1 * n_2
print('La multiplicacion da: ', '{:0.3f}'.format(mult))
