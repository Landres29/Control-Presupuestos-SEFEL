## Versión 1.1 - Mejoras de seguridad en inicio de sesión

**Versión anterior:** v1.0

**Nueva versión:** v1.1

**Tipo de cambio:**  
Corrección de defectos y mejora de seguridad.

**Motivo del cambio:**  
Durante la ejecución de los casos de prueba CP-001, CP-002 y CP-003 se detectaron problemas relacionados con el inicio de sesión y el control de acceso.

Los defectos identificados fueron:

- DEF-001 - Mensaje innecesario después del inicio de sesión.
- DEF-002 - Acceso permitido con usuario inexistente.
- DEF-003 - Acceso permitido con contraseña incorrecta.

**Cambios planificados para la versión 1.1:**

- Eliminar el mensaje de confirmación mostrado después de un inicio de sesión correcto.
- Validar que el usuario ingresado exista.
- Validar que la contraseña corresponda al usuario.
- Rechazar el acceso cuando las credenciales sean incorrectas.
- Mantener la validación de campos vacíos.
- Implementar un contador de intentos incorrectos.
- Bloquear temporalmente el inicio de sesión después de tres intentos fallidos consecutivos.
- Mostrar mensajes claros cuando las credenciales sean incorrectas o el acceso se encuentre bloqueado.

**Casos de prueba relacionados:**

- CP-001 - Inicio de sesión con credenciales válidas.
- CP-002 - Inicio de sesión con usuario inexistente.
- CP-003 - Inicio de sesión con contraseña incorrecta.
- CP-004 - Inicio de sesión con campos vacíos.
- CP-022 - Intentos incorrectos consecutivos de inicio de sesión.

**Estado:**  
Finalizado.

**Resultado esperado:**  
La versión 1.1 debe corregir los defectos encontrados en el módulo de inicio de sesión y mejorar el control de acceso antes de continuar con las siguientes pruebas del sistema.