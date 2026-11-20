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
En desarrollo.