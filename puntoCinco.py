#Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
#porcentaje de alumnos de cada uno de los cursos.

networkStudents = int(input("Ingresar número de estudiantes en redes: "))
contStudents = int(input("Ingresar número de estudiantes en contabilidad: "))
designStudents = int(input("Ingresar número de estudiantes en diseño: "))

totalStudents = networkStudents + contStudents + designStudents
networkPercentage = (networkStudents / totalStudents) * 100
contPercentage = (contStudents / totalStudents) * 100
designPercentage = (designStudents / totalStudents) * 100

print("El número total de estudiantes es de: ", totalStudents)
print("El porcentaje de estudiantes de redes es de: ", networkPercentage, "%")
print("El porcentaje de estudiantes de redes es de: ",contPercentage, "%")
print("El porcentaje de estudiantes de redes es de: ",designPercentage, "%")
