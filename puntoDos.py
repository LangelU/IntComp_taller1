#Haga un programa en Python que permita ingresar el dinero invertido por
#tres personas para formar una empresa. Cada una de ellas invierte una
#cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
#al total de la inversión

print("Porfavor ingresar el valor de la inversión de las 3 personas")
firstValue = int(input("Ingrese el valor aportado por la primera persona: "))
secondValue = int(input("Ingrese el valor aportado por la segunda persona: "))
thirdValue = int(input("Ingrese el valor aportado por la tercera persona: "))
totalValue = firstValue + secondValue + thirdValue
firstPercentage = round((firstValue / totalValue) * 100)
secondPercentage = round((secondValue / totalValue) * 100)
thirdPercentage = round((thirdValue / totalValue) * 100)
print("El valor total es de: ", totalValue)
print("El porcentaje aportado por la primera persona respecto al total es de: ", firstPercentage, "%")
print("El porcentaje aportado por la segunda persona respecto al total es de: ", secondPercentage, "%")
print("El porcentaje aportado por la tercera persona respecto al total es de: ", thirdPercentage, "%")