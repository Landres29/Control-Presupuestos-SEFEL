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
Pendiente de corrección.

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
Pendiente de corrección.

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
Pendiente de corrección.

**Corrección propuesta:**  
Implementar una validación real de la contraseña asociada al usuario antes de permitir el acceso al sistema. El acceso solo debe concederse cuando el usuario exista y la contraseña ingresada coincida con la registrada.

**Evidencia:**  
Capturas correspondientes al caso de prueba CP-003.