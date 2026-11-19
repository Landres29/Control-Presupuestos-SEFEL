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