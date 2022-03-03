#Una Institución educativa ha recibido una donación especial que será
#repartida entre las carreras de Telecomunicaciones, Sistemas,
#Administración y Contabilidad de la siguiente forma:
#a. Telecomunicaciones 10% del valor dado a sistemas
#b. Sistemas: 25% del valor dado a Administración
#c. Administración: 35% del valor de la donación
#d. Contabilidad: lo que resta de la donación

donation = int(input("Ingrese el valor de la donación: "))
admin_value = donation * 0.35
systems_value = admin_value * 0.25
comunication_value = systems_value * 0.10
contab_value = donation - (admin_value + systems_value + comunication_value)

print("El valor total ingresado fue de: ", donation, "pesos")
print("El valor que corresponde a telecomunicaciones es de: ", comunication_value, "pesos")
print("el valor que corresponde a sistemas es de: ", systems_value, "pesos")
print("El valor que correspnde a administración es de: ", admin_value, "pesos")
print("El valor que corresponde a contabilidad es de: ", contab_value, "pesos")