#Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
#ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
#total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
#en Python que permita mostrar el valor ganado por comisión y el valor total
#a pagar al vendedor.

salary = int(input("Ingrese el valor del sueldo: "))
sells = int(input("Ingrese el valor vendido durante el mes: "))
commision = sells * 0.15
total_value = salary + commision

print("El valor de la comisión es de: ", commision, "pesos")
print("El valor total a pagar es de: ", total_value, "pesos")