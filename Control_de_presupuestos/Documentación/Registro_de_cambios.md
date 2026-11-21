## Versión 1.1 - Mejoras de seguridad en inicio de sesión

**Cambios realizados para la versión 1.1:**

- Se eliminó el mensaje de confirmación mostrado después de un inicio de sesión correcto.
- Se agregó validación del usuario ingresado.
- Se agregó validación de la contraseña.
- Se rechazó el acceso cuando las credenciales son incorrectas.
- Se mantuvo la validación de campos vacíos.
- Se mejoraron los mensajes mostrados cuando las credenciales son incorrectas.

**Casos de prueba relacionados:**

- CP-001 - Inicio de sesión con credenciales válidas.
- CP-002 - Inicio de sesión con usuario inexistente.
- CP-003 - Inicio de sesión con contraseña incorrecta.
- CP-004 - Inicio de sesión con campos vacíos.

**Estado:**  
Finalizado.

**Resultado obtenido:**  
La versión 1.1 corrigió los defectos encontrados inicialmente en el módulo de inicio de sesión. Después de realizar las correcciones, se repitieron las pruebas y el sistema rechazó correctamente usuarios inexistentes, contraseñas incorrectas y campos vacíos, permitiendo el acceso únicamente con credenciales válidas.

**Mejoras pendientes para versiones posteriores:**  
El bloqueo temporal después de tres intentos fallidos consecutivos se deja pendiente para una versión futura del sistema.

## Versión 1.2 - Correcciones posteriores a las pruebas

**Versión anterior:** v1.1

**Nueva versión:** v1.2

**Tipo de cambio:**  
Corrección de defectos y mejoras funcionales.

**Cambios realizados:**

- Se corrigió DEF-006 agregando validación de formato y validez de fechas en el módulo de gastos.
- El sistema ahora exige fechas con formato `DD-MM-AAAA`.
- Se impide registrar fechas inexistentes, como `31-02-2026`.
- Se impide registrar fechas sin el formato establecido, como `01012006`.
- Se mantiene el registro normal de fechas válidas.

**Verificación de la corrección:**

Se repitió el caso de prueba relacionado después de modificar el código.

Resultados:

- `01012006` → rechazado correctamente.
- `31-02-2026` → rechazado correctamente.
- `18-11-2026` → aceptado correctamente.

**Resultado de la verificación:**  
Aprobado.

**Defectos corregidos hasta el momento:**

- DEF-006 - El sistema acepta fechas con formato inválido en gastos.

**Estado:**  
Finalizado.

## Versión 1.3 - Correcciones funcionales

**Versión anterior:** v1.2

**Nueva versión:** v1.3

**Tipo de cambio:**  
Corrección de defectos funcionales detectados durante las pruebas del sistema.

**Cambios realizados:**

-Se corrigió DEF-009, implementando correctamente la opción Cerrar sesión.
-Al cerrar sesión, la pantalla actual se limpia y el sistema vuelve al inicio de sesión.
-Se corrigió DEF-010, implementando el filtrado de obras mediante el campo Buscar obra.
-El buscador permite encontrar obras utilizando nombres completos o parciales.
-Al dejar vacío el campo de búsqueda, se vuelven a mostrar todas las obras.
-Se corrigió DEF-011, permitiendo acceder a la comparación de costos desde una obra seleccionada.
-Al hacer doble clic sobre una obra, el sistema abre el módulo de comparación de costos y selecciona automáticamente la obra consultada.

**Casos de prueba relacionados:**

-CP-018 - Cerrar sesión correctamente.
-CP-019 - Buscar una obra registrada.
-CP-020 - Acceder a los costos desde una obra.

**Verificación de la corrección:**

-La opción Cerrar sesión devuelve correctamente al usuario a la pantalla de inicio de sesión.
-El buscador filtra correctamente las obras mientras se escribe.
-La opción de consulta de costos permite abrir el módulo de comparación desde una obra seleccionada.

**Defectos corregidos hasta el momento:**

-DEF-009 - La opción Cerrar sesión no funciona.
-DEF-010 - El buscador de obras no filtra los resultados.
-DEF-011 - La opción Ver costos no funciona.

**Estado:**  
Finalizado.

## Versión 1.4 - Correcciones finales y mejoras de validación

**Versión anterior:** v1.3

**Nueva versión:** v1.4

**Tipo de cambio:**
Corrección de defectos y mejoras de validación y usabilidad.

**Cambios realizados:**

- Se corrigió DEF-008, agregando una comprobación de existencia de la base de datos antes de iniciar el sistema.
- Se evita la creación silenciosa de una nueva base de datos cuando sefel.db no está disponible.
- Se corrigió DEF-004, mejorando los mensajes de validación de montos en Presupuestos.
- Se corrigió DEF-005, mejorando los mensajes de validación de montos en Gastos.
- Se corrigió DEF-007, incorporando búsqueda de obras en la comparación de costos.
- Se mantuvieron las correcciones realizadas en versiones anteriores.

**Casos de prueba relacionados:**

- CP-008
- CP-009
- CP-010
- CP-012
- CP-013
- CP-015
- CP-017

**Estado:**
Finalizado.