# Sprint 4 - Comparación de costos y pruebas finales

## Objetivo

Implementar la comparación de costos entre los montos presupuestados y los gastos registrados de cada obra, además de realizar las pruebas necesarias para comprobar el funcionamiento general del prototipo.

## Actividades

Durante este Sprint se consideran las siguientes actividades:

- Implementar la comparación entre presupuestos y gastos.
- Obtener la información almacenada en la base de datos.
- Calcular la diferencia entre el monto presupuestado y el gasto real.
- Identificar el estado de cada obra según el resultado de la comparación.
- Mostrar los resultados de la comparación en una tabla.
- Revisar la navegación entre las diferentes pantallas.
- Comprobar el funcionamiento de las principales funcionalidades.
- Ejecutar pruebas funcionales.
- Ejecutar pruebas de seguridad definidas para el prototipo.
- Ejecutar pruebas de usabilidad.
- Registrar los errores o defectos encontrados.
- Corregir los defectos identificados.
- Realizar pruebas de regresión después de las correcciones.
- Preparar el prototipo para su revisión.

## Responsable

Equipo completo.

## Duración estimada

1 semana.

## Entregable

Prototipo funcional y pruebas.

## Funcionalidades implementadas

### Comparación de costos

El sistema utiliza la información de presupuestos y gastos almacenada en SQLite para realizar una comparación por obra.

Se consideran los siguientes valores:

- Presupuesto registrado.
- Gastos registrados.
- Diferencia entre presupuesto y gastos.
- Estado financiero de la obra.

La diferencia se calcula mediante:

**Diferencia = Presupuesto - Gastos**

Según el resultado:

- Una diferencia positiva indica que el gasto se encuentra bajo el presupuesto.
- Una diferencia negativa indica que los gastos superan el presupuesto.
- Una diferencia igual a cero indica equilibrio entre presupuesto y gastos.

### Consulta de resultados

Los resultados se presentan en una tabla que permite visualizar:

- Obra.
- Presupuesto.
- Gastos.
- Diferencia.
- Estado.

Los datos utilizados deben provenir de la base de datos y no de valores escritos directamente en el código.

## Pruebas del sistema

Durante este Sprint se realizará la etapa principal de pruebas del prototipo.

Se considerarán principalmente:

- Pruebas funcionales.
- Pruebas de seguridad.
- Pruebas de usabilidad.
- Pruebas de recuperación cuando corresponda.
- Pruebas de regresión después de realizar correcciones.

No se consideran pruebas de carga, estrés o rendimiento para esta etapa del proyecto.

## Niveles de prueba

Se trabajará con los siguientes niveles:

- Pruebas unitarias.
- Pruebas de integración.
- Pruebas de sistema.

La prueba de aceptación deberá ser realizada por un usuario o representante correspondiente.

## Registro de defectos

Los defectos encontrados durante las pruebas deberán registrarse indicando como mínimo:

- Identificador del defecto.
- Funcionalidad afectada.
- Descripción.
- Datos utilizados.
- Resultado esperado.
- Resultado obtenido.
- Nivel de severidad.
- Estado del defecto.
- Corrección realizada, cuando corresponda.

Los niveles de severidad serán definidos en el Plan de Pruebas.

## Seguridad

Durante este Sprint también se revisarán aspectos relacionados con:

- Confidencialidad.
- Integridad.
- Disponibilidad.
- Validación de usuarios.
- Rechazo de usuarios inexistentes.
- Control de intentos incorrectos de inicio de sesión.
- Manejo de errores y fallos del sistema.

Las medidas específicas serán implementadas y verificadas mediante sus respectivos casos de prueba.

## Control de versiones

Todos los cambios, correcciones y mejoras realizados durante este Sprint deberán registrarse mediante Git y GitHub.

Las correcciones importantes deberán quedar identificadas mediante commits separados para mantener la trazabilidad de los cambios realizados después de las pruebas.

## Revisión del Sprint

Al finalizar el Sprint se deberá comprobar:

- Que la comparación utilice datos reales almacenados en SQLite.
- Que los cálculos de presupuesto, gastos y diferencia sean correctos.
- Que el estado mostrado corresponda al resultado obtenido.
- Que las principales funcionalidades del sistema puedan utilizarse correctamente.
- Que los usuarios definidos para las pruebas se encuentren disponibles.
- Que los casos de prueba hayan sido ejecutados.
- Que los defectos encontrados estén registrados.
- Que los defectos críticos hayan sido corregidos antes de finalizar la etapa.
- Que las correcciones hayan sido verificadas mediante pruebas de regresión.
- Que los cambios realizados estén registrados en GitHub.

## Evidencias

Las evidencias correspondientes al Sprint pueden incluir:

- Historial de commits en GitHub.
- Capturas de la comparación de costos.
- Casos de prueba ejecutados.
- Resultados obtenidos.
- Registro de defectos.
- Evidencias antes y después de las correcciones.
- Resultados de las pruebas de regresión.
- Capturas del prototipo funcional.

## Estado

En desarrollo.