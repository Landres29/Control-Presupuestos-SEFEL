## DEF-001 - Mensaje innecesario después del inicio de sesión

**Caso de prueba relacionado:** CP-001

**Requerimiento relacionado:** RF-01 / RNF-01

**Funcionalidad afectada:** Inicio de sesión

**Descripción del defecto:**  
Después de ingresar credenciales válidas, el sistema muestra un mensaje de confirmación antes de abrir la pantalla principal.

El inicio de sesión funciona correctamente, pero este mensaje se considera innecesario porque agrega un paso adicional y retrasa el acceso directo al sistema.

**Resultado esperado:**  
Al validar correctamente las credenciales, el sistema debería ingresar directamente a la pantalla principal.

**Resultado obtenido:**  
El sistema valida las credenciales, muestra un mensaje de acceso y posteriormente permite ingresar a la pantalla principal.

**Tipo de defecto:**  
Usabilidad.

**Severidad:**  
Baja.

**Estado:**  
Corregido

**Corrección propuesta:**  
Eliminar el mensaje de confirmación posterior al inicio de sesión y abrir directamente la pantalla principal cuando las credenciales sean correctas.

**Evidencia:**  
Captura correspondiente al caso de prueba CP-001.

## DEF-002 - Acceso permitido con usuario inexistente

**Caso de prueba relacionado:** CP-002

**Requerimiento relacionado:** RF-01 / RF-10

**Funcionalidad afectada:** Inicio de sesión / Control de acceso

**Descripción del defecto:**  
Al ingresar un usuario que no se encuentra registrado en el sistema junto con una contraseña cualquiera, el sistema permite continuar con el inicio de sesión.

Durante la prueba se utilizó el usuario `usuario999` y la contraseña `prueba123`. El sistema mostró el mensaje “Credenciales ingresadas.” y posteriormente permitió acceder a la pantalla principal.

Este comportamiento representa un problema de seguridad, ya que un usuario inexistente no debería poder ingresar al sistema.

**Resultado esperado:**  
El sistema debería rechazar el acceso cuando el usuario ingresado no se encuentre registrado y mostrar un mensaje indicando que las credenciales no son válidas.

**Resultado obtenido:**  
El sistema aceptó las credenciales ingresadas, mostró un mensaje de confirmación y permitió acceder a la pantalla principal.

**Tipo de defecto:**  
Seguridad / Funcionalidad.

**Severidad:**  
Crítica.

**Estado:**  
Corregido.

**Corrección propuesta:**  
Implementar una validación real de las credenciales antes de permitir el acceso al sistema. El usuario ingresado debe existir y la contraseña debe coincidir con la registrada.

**Evidencia:**  
Capturas correspondientes al caso de prueba CP-002.

## DEF-003 - Acceso permitido con contraseña incorrecta

**Caso de prueba relacionado:** CP-003

**Requerimiento relacionado:** RF-01 / RF-10

**Funcionalidad afectada:** Inicio de sesión / Control de acceso

**Descripción del defecto:**  
Al ingresar un usuario válido junto con una contraseña incorrecta, el sistema permite continuar con el inicio de sesión.

Durante la prueba se utilizó el usuario `admin` y la contraseña incorrecta `321`. El sistema mostró el mensaje “Credenciales ingresadas.” y posteriormente permitió acceder a la pantalla principal.

Este comportamiento representa un problema de seguridad, ya que un usuario no debería poder ingresar al sistema si la contraseña no coincide con la registrada.

**Resultado esperado:**  
El sistema debería rechazar el acceso cuando la contraseña ingresada sea incorrecta y mostrar un mensaje indicando que las credenciales no son válidas.

**Resultado obtenido:**  
El sistema aceptó las credenciales, mostró un mensaje de confirmación y permitió acceder a la pantalla principal a pesar de que la contraseña era incorrecta.

**Tipo de defecto:**  
Seguridad / Funcionalidad.

**Severidad:**  
Crítica.

**Estado:**  
Corregido.

**Corrección propuesta:**  
Implementar una validación real de la contraseña asociada al usuario antes de permitir el acceso al sistema. El acceso solo debe concederse cuando el usuario exista y la contraseña ingresada coincida con la registrada.

**Evidencia:**  
Capturas correspondientes al caso de prueba CP-003.

## DEF-004 - Mensaje poco específico al ingresar monto negativo

**Caso de prueba relacionado:** CP-008 / CP-009 / CP-010

**Requerimiento relacionado:** RF-04 / RNF-01

**Funcionalidad afectada:** Registro de presupuestos

**Descripción del defecto:**  
Al ingresar un monto negativo, cero o con letras en el registro de presupuesto, el sistema rechaza correctamente el valor, pero muestra el mensaje “El monto debe ser un número mayor que cero.”.

Aunque la validación funciona, el mensaje no diferencia claramente entre un monto negativo y otros tipos de valores inválidos, como un monto igual a cero o un campo vacío.

**Resultado esperado:**  
El sistema debería mostrar un mensaje específico para el tipo de error detectado.

Por ejemplo:

- Campo vacío: “Debe ingresar un monto.”
- Monto igual a cero: “El monto debe ser mayor que cero.”
- Monto negativo: “El monto no puede ser negativo.”
- Valor no numérico: “El monto debe ser un valor numérico.”

**Resultado obtenido:**  
El sistema rechazó correctamente el monto negativo, pero mostró un mensaje genérico que también puede utilizarse para otros valores inválidos.

**Tipo de defecto:**  
Usabilidad.

**Severidad:**  
Baja.

**Estado:**  
Pendiente de corrección.

**Corrección propuesta:**  
Modificar la validación del campo monto para mostrar mensajes diferentes según el error detectado, facilitando que el usuario comprenda por qué el valor ingresado fue rechazado.

**Evidencia:**  
Capturas correspondientes al caso de prueba CP-008, CP-009, CP-010.

## DEF-005 - Mensaje poco específico al ingresar monto negativo en gastos

**Caso de prueba relacionado:** CP-012 / CP-013

**Requerimiento relacionado:** RF-06 / RNF-01

**Funcionalidad afectada:** Registro de gastos

**Descripción del defecto:**  
Al ingresar un monto negativo en el registro de gastos, el sistema rechaza correctamente el valor, pero muestra el mensaje “El monto debe ser un número mayor que cero.”.

La validación funciona, pero el mensaje no indica de forma específica que el problema corresponde al ingreso de un monto negativo.

**Resultado esperado:**  
El sistema debería rechazar el registro y mostrar un mensaje específico, por ejemplo: “El monto no puede ser negativo.”.

**Resultado obtenido:**  
El sistema rechazó correctamente el monto negativo, pero mostró un mensaje genérico que también puede utilizarse para otros valores inválidos.

**Tipo de defecto:**  
Usabilidad.

**Severidad:**  
Baja.

**Estado:**  
Pendiente de corrección.

**Corrección propuesta:**  
Modificar la validación del monto en el módulo de gastos para mostrar mensajes distintos según el tipo de error detectado.

Por ejemplo:

- Campo vacío: “Debe ingresar un monto.”
- Monto igual a cero: “El monto debe ser mayor que cero.”
- Monto negativo: “El monto no puede ser negativo.”
- Valor no numérico: “El monto debe ser un valor numérico.”

**Evidencia:**  
Captura correspondiente al caso de prueba CP-012 / CP-013

## DEF-006 - El sistema acepta fechas con formato inválido en gastos

**Caso de prueba relacionado:** CP-014

**Requerimiento relacionado:** RF-06 / RF-09

**Funcionalidad afectada:** Registro de gastos / Validación de fecha

**Descripción del defecto:**  
Al ingresar una fecha que no cumple con el formato definido para el sistema, el registro de gasto es aceptado igualmente.

Durante la prueba se ingresó la fecha `01012006`, sin separadores y sin respetar el formato esperado. El sistema guardó el gasto y mostró el mensaje “El gasto se guardó correctamente.”.

Este comportamiento puede generar información inconsistente en los registros de gastos.

**Resultado esperado:**  
El sistema debería rechazar la fecha cuando no cumpla con el formato establecido y mostrar un mensaje indicando el formato correcto que debe utilizarse.

Por ejemplo:

`La fecha debe tener el formato DD-MM-AAAA.`

**Resultado obtenido:**  
El sistema aceptó la fecha `01012006` y registró el gasto correctamente.

**Tipo de defecto:**  
Funcionalidad / Validación.

**Severidad:**  
Media.

**Estado:**  
Corregido.

**Corrección propuesta:**  
Implementar una validación del campo fecha antes de guardar el gasto.

El sistema deberá comprobar que la fecha:

- Cumpla con el formato definido.
- Corresponda a una fecha válida.
- No contenga valores imposibles.

Si la fecha no es válida, se deberá impedir el registro y mostrar un mensaje claro al usuario.

**Evidencia:**  
Capturas correspondientes al caso de prueba CP-014.

## DEF-007 - Pantalla de comparación de costos poco intuitiva

**Caso de prueba relacionado:** CP-015

**Requerimiento relacionado:** RF-07 / RNF-01

**Funcionalidad afectada:** Comparación de costos

**Descripción del defecto:**  
La pantalla de comparación de costos muestra correctamente la información de presupuesto, gastos, diferencia y estado de cada obra, pero presenta pocas opciones de interacción para el usuario.

Actualmente, la pantalla solo muestra una tabla con los resultados y no incluye controles visibles que permitan filtrar, seleccionar una obra de manera clara o acceder a información más detallada.

Esto puede dificultar el uso del módulo cuando exista una mayor cantidad de obras registradas.

**Resultado esperado:**  
El módulo debería permitir consultar la información de manera más intuitiva, facilitando la selección y búsqueda de una obra y mostrando opciones claras para revisar su información.

**Resultado obtenido:**  
El sistema muestra correctamente la comparación de costos en una tabla, pero no presenta opciones adicionales de consulta o interacción.

**Tipo de defecto:**  
Usabilidad.

**Severidad:**  
Baja.

**Estado:**  
Pendiente de corrección.

**Corrección propuesta:**  
Mejorar la interfaz del módulo de comparación de costos incorporando opciones que faciliten la consulta de información.

Por ejemplo:

- Agregar un buscador de obras.
- Permitir seleccionar una obra específica.
- Incorporar una opción para visualizar el detalle de costos.
- Mantener claramente identificados el presupuesto, los gastos, la diferencia y el estado.
- Mejorar la presentación visual de los resultados.

**Evidencia:**  
Captura correspondiente al caso de prueba CP-015.

## DEF-009 - La opción Cerrar sesión no funciona

**Caso de prueba relacionado:** CP-018

**Requerimiento relacionado:** RF-01 / RF-10

**Funcionalidad afectada:** Cierre de sesión / Control de acceso

**Descripción del defecto:**  
Al presionar la opción `Cerrar sesión`, el sistema no realiza ninguna acción y el usuario permanece dentro de la aplicación.

Esto impide finalizar correctamente la sesión actual y obliga al usuario a cerrar completamente el programa para salir del sistema.

**Resultado esperado:**  
Al seleccionar `Cerrar sesión`, el sistema debería finalizar la sesión actual y volver a mostrar la pantalla de inicio de sesión.

Para volver a acceder a las funcionalidades, el usuario debería ingresar nuevamente credenciales válidas.

**Resultado obtenido:**  
La opción `Cerrar sesión` no ejecutó ninguna acción y el usuario permaneció en la pantalla principal.

**Tipo de defecto:**  
Funcionalidad / Seguridad.

**Severidad:**  
Media.

**Estado:**  
Pendiente de corrección.

**Corrección propuesta:**  
Implementar la funcionalidad del botón `Cerrar sesión` para que cierre la sesión actual y redirija al usuario a la pantalla de inicio de sesión.

Además, se debe comprobar que las pantallas internas no puedan seguir utilizándose sin volver a autenticarse.

**Evidencia:**  
Captura correspondiente al caso de prueba CP-018.

## DEF-010 - El buscador de obras no filtra los resultados

**Caso de prueba relacionado:** CP-019

**Requerimiento relacionado:** RF-03 / RNF-01

**Funcionalidad afectada:** Consulta de obras / Buscador

**Descripción del defecto:**  
El campo `Buscar obra` permite ingresar texto, pero no modifica ni filtra la lista de obras mostrada en pantalla.

Durante la prueba se ingresó `Obra Prueba 1`, pero el sistema continuó mostrando todas las obras registradas.

Esto genera una función visible que actualmente no cumple con el comportamiento esperado.

**Resultado esperado:**  
Al ingresar el nombre completo o parcial de una obra, el sistema debería filtrar la lista y mostrar únicamente los registros que coincidan con el texto ingresado.

**Resultado obtenido:**  
El sistema permitió escribir en el campo de búsqueda, pero la lista de obras no cambió y continuó mostrando todos los registros.

**Tipo de defecto:**  
Funcionalidad / Usabilidad.

**Severidad:**  
Media.

**Estado:**  
Pendiente de corrección.

**Corrección propuesta:**  
Implementar la lógica de búsqueda para que la tabla de obras se actualice según el texto ingresado.

La búsqueda debería permitir, como mínimo:

- Buscar por nombre completo.
- Buscar utilizando parte del nombre.
- Actualizar la lista mientras se escribe o al confirmar la búsqueda.
- Volver a mostrar todas las obras cuando el campo quede vacío.

**Evidencia:**  
Captura correspondiente al caso de prueba CP-019.

## DEF-011 - La opción Ver costos no funciona

**Caso de prueba relacionado:** CP-020

**Requerimiento relacionado:** RF-03 / RF-07

**Funcionalidad afectada:** Consulta de obras / Comparación de costos

**Descripción del defecto:**  
En la pantalla principal de obras aparece la opción `Ver costos` asociada a cada obra registrada.

Sin embargo, al seleccionar una obra e intentar utilizar dicha opción, el sistema no realiza ninguna acción y no permite acceder a la información de costos correspondiente.

Esto genera confusión, ya que la interfaz presenta `Ver costos` como una acción disponible, pero actualmente no tiene funcionalidad asociada.

**Resultado esperado:**  
Al seleccionar `Ver costos`, el sistema debería permitir consultar los costos de la obra seleccionada o dirigir al usuario al módulo de comparación mostrando la información correspondiente a esa obra.

**Resultado obtenido:**  
La obra puede seleccionarse en la tabla, pero la opción `Ver costos` no responde y no permite acceder a información adicional.

**Tipo de defecto:**  
Funcionalidad / Usabilidad.

**Severidad:**  
Media.

**Estado:**  
Pendiente de corrección.

**Corrección propuesta:**  
Implementar la funcionalidad asociada a la opción `Ver costos`.

Al utilizarla, el sistema debería:

- Identificar la obra seleccionada.
- Abrir el módulo de comparación de costos.
- Mostrar o destacar la información correspondiente a la obra seleccionada.
- Evitar mostrar acciones en la interfaz que no tengan funcionalidad implementada.

**Evidencia:**  
Captura correspondiente al caso de prueba CP-020.