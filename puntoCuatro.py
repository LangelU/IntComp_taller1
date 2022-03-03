#Un alumno desea saber cuál será su calificación final en la materia de
#fundamentos de programación. Dicha calificación se compone de los
#siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
#calificación de un examen en clase y 20% de la calificación de un proyecto
#final.

from unicodedata import decimal


print("Favor igresar las notas")
workshop = float(input("Ingresar el promedio de los talleres en clase: "))
quiz = float(input("Ingresar la nota del exámen en clase: "))
project = float(input("Ingresar la nota del proyecto final: "))

workshop_value = workshop * 0.50
quiz_value = quiz * 0.30
project_value = project * 0.20

final_note = workshop_value + quiz_value + project_value
rounded_note = round(final_note, 2)
if(final_note <= 3.0): {
    print("La nota final es de: ", rounded_note, ". El estudiante no aprobó")
} 
else: {
    print("La nota final es de: ", rounded_note, ". El estudiante aprobó")
}
