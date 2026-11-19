# Sprint 1 - Base de datos, registro de obras e inicio de sesión

## Objetivo

Diseñar la base de datos inicial del sistema e implementar las primeras funcionalidades necesarias para comenzar a trabajar con la información de las obras de SEFEL.

## Actividades

Durante este Sprint se consideran las siguientes actividades:

- Diseñar la estructura inicial de la base de datos.
- Implementar la conexión con SQLite.
- Crear el registro de obras.
- Permitir consultar las obras registradas.
- Implementar la pantalla de inicio de sesión.
- Crear la pantalla principal de la aplicación.
- Verificar que los datos de las obras permanezcan guardados al cerrar y volver a abrir el sistema.

## Responsable

Desarrollador y diseñador.

## Duración estimada

1 semana.

## Entregable

Registro de obras e inicio de sesión.

## Funcionalidades implementadas

### Inicio de sesión

Se implementa una pantalla de acceso que permite ingresar un nombre de usuario y una contraseña para acceder al sistema.

En esta primera etapa, el inicio de sesión corresponde a una implementación inicial y será mejorado posteriormente mediante usuarios registrados, validación de credenciales y controles de seguridad.

### Registro de obras

Se implementa un formulario que permite registrar una obra indicando:

- Nombre de la obra.
- Descripción.

La información registrada se almacena utilizando una base de datos SQLite.

### Consulta de obras

Las obras registradas se muestran en la pantalla principal de la aplicación.

El sistema permite visualizar los registros almacenados y comprobar que la información permanece disponible después de cerrar y volver a ejecutar el programa.

### Base de datos

Se utiliza SQLite como sistema de almacenamiento local.

En esta etapa se crea la estructura inicial necesaria para almacenar la información de las obras y posteriormente relacionarla con presupuestos y gastos.

## Validaciones iniciales

Durante el registro de obras se consideran las siguientes validaciones básicas:

- El nombre de la obra no puede estar vacío.
- El sistema debe mostrar un mensaje cuando falta información obligatoria.
- Los datos registrados deben permanecer almacenados después de reiniciar la aplicación.

Las validaciones más específicas serán definidas posteriormente en los requerimientos y casos de prueba.

## Control de versiones

Los avances realizados durante el Sprint se registran mediante Git y GitHub.

Los commits relacionados con este Sprint permiten demostrar la evolución desde la primera pantalla de inicio de sesión hasta la incorporación de la base de datos y el registro persistente de obras.

## Revisión del Sprint

Al finalizar el Sprint se debe comprobar:

- Que la aplicación pueda iniciarse correctamente.
- Que la pantalla de inicio de sesión se muestre correctamente.
- Que se pueda acceder a la pantalla principal.
- Que se pueda registrar una obra.
- Que la obra aparezca en la tabla.
- Que la información permanezca guardada al cerrar y volver a abrir la aplicación.
- Que los cambios realizados estén registrados en GitHub.

## Evidencias

Las evidencias correspondientes al Sprint pueden incluir:

- Historial de commits en GitHub.
- Capturas de la pantalla de inicio de sesión.
- Capturas de la pantalla principal.
- Capturas del formulario de registro de obras.
- Registros almacenados en la base de datos.
- Resultados de las pruebas realizadas.

## Estado

Finalizado.