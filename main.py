import os

nombreTrabajador = input("Ingrese nombre del trabajador: ")
sueldoBasico = float (input('Ingrese el valor del sueldo basico: '))
diasFalta = float (input('Ingrese los dias de falta: '))
minutosTardanza = float (input('Ingrese los minutos de tardanza: '))
horasExtras = float (input('Ingrese las horas extras: '))
bonificacionMovilidad = 1000
bonificacionSuplementaria = 0.03*sueldoBasico
CostoHoraNormal = sueldoBasico/240
CostoHoraExtra = 1.5*CostoHoraNormal
bonificacionHoraExtra = horasExtras*CostoHoraExtra
bonificaciones = bonificacionMovilidad + bonificacionSuplementaria + bonificacionHoraExtra
descuentos = diasFalta+minutosTardanza
sueldoNeto = sueldoBasico + bonificaciones-descuentos

os.system ('pause')

print('                         Boleta de pago de '+ nombreTrabajador)
print('El sueldo basico es: ' + repr (sueldoBasico))
print('La bonificacion es: ' + repr (bonificaciones))
print('Los descuentos son:-' + repr (descuentos))
print('El sueldo neto es: ' + repr (sueldoNeto))
