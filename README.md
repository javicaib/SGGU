# Trabajo de curso de Ingeniería de Software  y Programación web

## Descripción del sistema a desarrollar
La planificación de la guardia estudiantil es un proceso clave en la UCI, de la calidad de esta depende la integridad de la universidad, así como reducir los niveles de riesgo que se puedan dar.
El encargado de planificar la guardia tiene como misión gestionar la guardia, teniendo en cuenta personal y horarios. Una vez esto se realice teniendo en cuenta que no se repitan estudiantes en los mismos turnos y días, los supervisores tienen la opción de registrar las incidencias de la guardia y evaluar el comportamiento de los estudiantes en la misma.

## Requisitos funcionales

1. RF_Autenticar
2. RF_Gestionar Estudiantes
3. RF_Gestionar Incidencias
4. RF_Gestionar Grupos de guardia

## Requisitos no funcionales
* RNF1: La interfaz debe ser amigable y fácil de usar, de manera que no sea una dificultad para los usuarios el trabajo con la misma.
* RNF2: Las interfaces tienen que ostentar un diseño sencillo, con pocas entradas, permitiendo un balance adecuado entre funcionalidad y simplicidad de tal manera que no se haga difícil para los usuarios la utilización del sistema.
* RNF3: El sistema a utilizar se debe desarrollar en Python 3, sobre el framework de desarrollo web Django.
RNF4: El sistema debe contar con una base de datos implementada en PostgreSQL.
* RNF5: El código debe ser reutilizable.
* RNF6: La aplicación debe ser web y estar disponible las 24 horas del día.
* RNF7: La aplicación debe soportar el crecimiento del volumen de usuarios y roles.
* RNF8: El sistema debe emplear el protocolo HTTPS para cifrar los datos que 
Viajan entre máquinas.

## Pasos para iniciar el proyecto

### Instalar los requisitos
`pip install -r requirements.txt ` 

### Ejecutar el proyecto
` python manage.py runserver`