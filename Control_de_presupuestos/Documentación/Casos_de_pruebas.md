Casos de Prueba del Sistema

1. Objetivo

Definir los casos de prueba que serán utilizados para verificar el funcionamiento del prototipo de Control de Presupuestos SEFEL.

Cada caso de prueba se relaciona con uno o más requerimientos definidos en Requerimientos.md.

Los casos serán ejecutados durante el Sprint 4 y sus resultados permitirán identificar posibles defectos del sistema.

2. Estados posibles

Cada caso de prueba podrá tener uno de los siguientes estados:

Pendiente: todavía no ha sido ejecutado.

Aprobado: el resultado obtenido coincide con el resultado esperado.

Fallido: el resultado obtenido no coincide con el esperado.

Cuando un caso falle, el problema encontrado deberá registrarse en Registro_de_defectos.md.

3. Casos de prueba de inicio de sesión

CP-001 - Inicio de sesión con credenciales válidas

Requerimiento: RF-01 / RF-10

Objetivo:
Comprobar que un usuario registrado pueda ingresar al sistema utilizando credenciales correctas.

Datos de entrada:

Usuario: usuario válido registrado.

Contraseña: contraseña correcta.

Pasos:

Ejecutar la aplicación.

Ingresar un usuario válido.

Ingresar la contraseña correcta.

Presionar el botón de inicio de sesión.

Resultado esperado:

El sistema debe permitir el acceso y mostrar la pantalla principal.

Resultado obtenido:

Pendiente de ejecución.

Estado:

Pendiente.

Evidencia:

Pendiente.

CP-002 - Inicio de sesión con usuario inexistente

Requerimiento: RF-01 / RF-10

Objetivo:
Comprobar que el sistema rechace un usuario que no se encuentre registrado.

Datos de entrada:

Usuario: usuario inexistente.

Contraseña: cualquier contraseña.

Pasos:

Ejecutar la aplicación.

Ingresar un usuario inexistente.

Ingresar una contraseña.

Presionar el botón de inicio de sesión.

Resultado esperado:

El sistema debe rechazar el acceso y mostrar un mensaje indicando que las credenciales no son válidas.

Resultado obtenido:

Pendiente de ejecución.

Estado:

Pendiente.

Evidencia:

Pendiente.

CP-003 - Inicio de sesión con contraseña incorrecta

Requerimiento: RF-01 / RF-10

Objetivo:
Comprobar que un usuario existente no pueda ingresar utilizando una contraseña incorrecta.

Datos de entrada:

Usuario: usuario válido.

Contraseña: contraseña incorrecta.

Pasos:

Ejecutar la aplicación.

Ingresar un usuario existente.

Ingresar una contraseña incorrecta.

Presionar el botón de inicio de sesión.

Resultado esperado:

El sistema debe rechazar el acceso y mostrar un mensaje de credenciales incorrectas.

Resultado obtenido:

Pendiente de ejecución.

Estado:

Pendiente.

Evidencia:

Pendiente.

CP-004 - Inicio de sesión con campos vacíos

Requerimiento: RF-01

Objetivo:
Comprobar que no sea posible iniciar sesión dejando campos obligatorios vacíos.

Datos de entrada:

Usuario: vacío.

Contraseña: vacía.

Pasos:

Ejecutar la aplicación.

Dejar los campos de usuario y contraseña vacíos.

Presionar el botón de inicio de sesión.

Resultado esperado:

El sistema debe impedir el acceso y mostrar un mensaje indicando que los campos son obligatorios.

Resultado obtenido:

Pendiente de ejecución.

Estado:

Pendiente.

Evidencia:

Pendiente.