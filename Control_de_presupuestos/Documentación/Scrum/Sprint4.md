# Sprint 4 - Comparación de costos y pruebas finales

## Objetivo

Implementar la comparación de costos entre los montos presupuestados y los gastos registrados de cada obra, además de ejecutar las pruebas necesarias para comprobar el funcionamiento general del prototipo.

## Actividades realizadas

Durante este Sprint se realizaron las siguientes actividades:

- Implementación de la comparación entre presupuestos y gastos.
- Obtención de información almacenada en SQLite.
- Cálculo de la diferencia entre el monto presupuestado y los gastos reales.
- Identificación del estado de cada obra según el resultado de la comparación.
- Presentación de los resultados mediante una tabla.
- Revisión de la navegación entre las diferentes pantallas.
- Pruebas de las funcionalidades principales.
- Ejecución de pruebas funcionales.
- Ejecución de pruebas de seguridad correspondientes al alcance del prototipo.
- Ejecución de pruebas de usabilidad.
- Pruebas de persistencia y manejo de fallos.
- Registro de errores y defectos encontrados.
- Clasificación de los defectos según su severidad.
- Corrección de los defectos detectados.
- Repetición de las pruebas después de las correcciones.
- Registro de los cambios mediante Git y GitHub.
- Preparación del prototipo para su revisión final.

## Responsable

**Equipo completo.**

## Duración estimada

**1 semana.**

## Entregable

**Prototipo funcional y pruebas.**

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

- Una diferencia positiva corresponde a **Superávit**.
- Una diferencia negativa corresponde a **Déficit**.
- Una diferencia igual a cero corresponde a **Equilibrado**.

### Consulta de resultados

Los resultados se presentan en una tabla que permite visualizar:

- Obra.
- Presupuesto.
- Gastos.
- Diferencia.
- Estado.

Los valores utilizados provienen de los registros almacenados en SQLite.

Como mejora de usabilidad, el módulo de comparación permite buscar una obra utilizando su nombre completo o parcial.

Además, desde la pantalla principal es posible seleccionar una obra y acceder directamente a su información de comparación mediante doble clic.

## Pruebas del sistema

Durante este Sprint se ejecutó la etapa principal de pruebas del prototipo.

Se realizaron principalmente:

- Pruebas funcionales.
- Pruebas de seguridad.
- Pruebas de usabilidad.
- Pruebas de persistencia.
- Pruebas de recuperación.
- Pruebas de regresión después de realizar correcciones.

No se realizaron pruebas de carga, estrés ni rendimiento avanzado, debido a que no forman parte del alcance definido para este prototipo.

## Niveles de prueba considerados

Se trabajó principalmente con:

- Pruebas unitarias sobre funciones y validaciones específicas.
- Pruebas de integración entre interfaz, lógica y SQLite.
- Pruebas de sistema utilizando el flujo completo del prototipo.

La prueba de aceptación corresponde a un usuario o representante y se considera una actividad independiente de las pruebas realizadas por el equipo de desarrollo.

## Registro de defectos

Los defectos encontrados durante las pruebas fueron registrados en `Registro_de_defectos.md`.

Para cada defecto se documentó, según correspondía:

- Identificador.
- Caso de prueba relacionado.
- Requerimiento relacionado.
- Funcionalidad afectada.
- Descripción.
- Resultado esperado.
- Resultado obtenido.
- Tipo de defecto.
- Severidad.
- Estado.
- Corrección realizada.
- Evidencia.

Durante las pruebas se detectaron defectos relacionados con:

- Inicio de sesión.
- Validación de credenciales.
- Mensajes de validación de montos.
- Validación de fechas.
- Usabilidad de la comparación de costos.
- Manejo de ausencia de la base de datos.
- Cierre de sesión.
- Búsqueda de obras.
- Acceso a la comparación desde una obra.

Los defectos incluidos dentro del alcance actual fueron corregidos y posteriormente verificados.

## Seguridad

Durante este Sprint se revisaron principalmente:

- Validación de usuario y contraseña.
- Rechazo de usuarios inexistentes.
- Rechazo de contraseñas incorrectas.
- Control de acceso.
- Cierre de sesión.
- Integridad de los datos.
- Persistencia de la información.
- Manejo de ausencia de la base de datos.

**Mejora futura:**  
El bloqueo temporal después de varios intentos fallidos de inicio de sesión no forma parte de la versión actual y queda considerado como una posible mejora para una versión futura.

## Control de versiones

Los cambios, correcciones y mejoras realizados durante el Sprint fueron registrados mediante Git y GitHub.

Se utilizaron commits separados para identificar las principales correcciones realizadas después de las pruebas.

Esto permite mantener trazabilidad entre:

**Prueba → Defecto → Corrección → Commit**

## Revisión del Sprint

Al finalizar el Sprint se comprobó:

- Que la comparación utiliza información almacenada en SQLite.
- Que los cálculos de presupuesto, gastos y diferencia son correctos.
- Que el estado mostrado corresponde al resultado calculado.
- Que las principales funcionalidades pueden utilizarse correctamente.
- Que el inicio de sesión valida las credenciales.
- Que las validaciones de montos funcionan correctamente.
- Que las fechas inválidas son rechazadas.
- Que los datos permanecen almacenados después de reiniciar la aplicación.
- Que el sistema informa cuando la base de datos original no está disponible.
- Que el cierre de sesión funciona correctamente.
- Que la búsqueda de obras funciona.
- Que es posible acceder a la comparación desde una obra.
- Que el buscador de la comparación funciona.
- Que los casos de prueba principales fueron ejecutados.
- Que los defectos encontrados fueron registrados.
- Que los defectos críticos encontrados fueron corregidos.
- Que las correcciones fueron verificadas mediante nuevas ejecuciones de las pruebas.
- Que los cambios realizados quedaron registrados mediante Git y GitHub.

## Evidencias

Las evidencias del Sprint incluyen:

- Historial de commits en GitHub.
- Capturas del prototipo.
- Capturas de la comparación de costos.
- Casos de prueba ejecutados.
- Resultados obtenidos.
- Registro de defectos.
- Evidencias anteriores y posteriores a las correcciones.
- Verificación de las correcciones.
- Documento Word con capturas y evidencias de las pruebas.

## Resultado del Sprint

Se obtuvo un prototipo funcional capaz de:

- Gestionar obras.
- Registrar presupuestos.
- Registrar gastos.
- Mantener información mediante SQLite.
- Comparar presupuestos y gastos.
- Identificar superávit, déficit o equilibrio.
- Validar los principales datos ingresados.
- Controlar el acceso mediante inicio y cierre de sesión.
- Buscar obras.
- Acceder a los costos de una obra.
- Manejar de forma controlada la ausencia de la base de datos.

Los defectos identificados durante las pruebas y considerados dentro del alcance actual fueron corregidos.

## Estado

**Finalizado.**