import pandas as pd
from academico.models import Profesor, Estudiante, EncuestaProfesor, EncuestaEstudiante

def cargar_encuesta_profesores_desde_excel(archivo):
    data = pd.read_excel(archivo)
    for _, row in data.iterrows():
        profesor, _ = Profesor.objects.get_or_create(nombre=row['profesor'])
        EncuestaProfesor.objects.create(
            profesor=profesor,
            preguntas={
                'pregunta_1': row['pregunta_1'],
                'pregunta_2': row['pregunta_2'],
                'pregunta_3': row['pregunta_3'],
                # Agrega más preguntas según las columnas del Excel
            }
        )


def cargar_encuesta_estudiantes_desde_excel(archivo):
    data = pd.read_excel(archivo)
    for _, row in data.iterrows():
        estudiante, _ = Estudiante.objects.get_or_create(nombre=row['estudiante'])
        EncuestaEstudiante.objects.create(
            estudiante=estudiante,
            preguntas={
                'pregunta_1': row['pregunta_1'],
                'pregunta_2': row['pregunta_2'],
                'pregunta_3': row['pregunta_3'],
                # Agrega más preguntas según las columnas del Excel
            }
        )