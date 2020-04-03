#Datos
#precio del producto
#al final muestre precio final del iva

print('Calculo de IVA')
precio = float(input('Ingresa el precio del producto: '))
calculo_total_iva = precio * 1.16
iva = precio * 0.16
print('El IVA del producto es ', iva )
print('El precio del producto con IVA es: ','{:0.2f}'.format(calculo_total_iva))
