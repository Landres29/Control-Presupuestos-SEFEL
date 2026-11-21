# Casos de Prueba del Sistema

## 1. Objetivo

Definir y registrar los casos de prueba utilizados para verificar el funcionamiento del prototipo de **Control de Presupuestos SEFEL**.

Cada caso de prueba se relaciona con uno o más requerimientos definidos en `Requerimientos.md`.

Las pruebas fueron ejecutadas principalmente durante el **Sprint 4** y permitieron comprobar las funcionalidades del sistema, detectar defectos, aplicar correcciones y verificar posteriormente su funcionamiento.

**Evidencias:**  
Las evidencias detalladas de la ejecución de las pruebas se mantienen en un documento Word junto con las capturas correspondientes.

## 2. Estados posibles

Cada caso de prueba puede presentar uno de los siguientes estados:

- **Pendiente:** todavía no ha sido ejecutado.
- **Aprobado:** el resultado obtenido coincide con el resultado esperado.
- **Fallido:** el resultado obtenido no coincide con el esperado.
- **Aprobado después de corrección:** inicialmente se detectó un problema, se realizó una corrección y posteriormente la prueba fue ejecutada nuevamente de forma satisfactoria.

Cuando una prueba presenta un fallo, el defecto correspondiente se registra en `Registro_de_defectos.md`.

## 3. Casos de prueba

### CP-001 - Inicio de sesión con credenciales válidas

**Requerimiento relacionado:**  
RF-01 / RF-10

**Objetivo:**  
Comprobar que un usuario con credenciales válidas pueda acceder al sistema.

**Datos utilizados:**

- Usuario: `admin`
- Contraseña: `123`

**Resultado esperado:**  
El sistema debe permitir el acceso y mostrar directamente la pantalla principal.

**Resultado final:**  
El usuario puede ingresar correctamente y ya no se muestra un mensaje innecesario antes de acceder.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-001.

### CP-002 - Inicio de sesión con usuario inexistente

**Requerimiento relacionado:**  
RF-01 / RF-10

**Objetivo:**  
Comprobar que un usuario inexistente no pueda ingresar al sistema.

**Datos utilizados:**

- Usuario: `usuario999`
- Contraseña: `prueba123`

**Resultado esperado:**  
El sistema debe rechazar el acceso.

**Resultado inicial:**  
El sistema permitía ingresar.

**Resultado final:**  
El sistema rechaza correctamente las credenciales.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-002.

### CP-003 - Inicio de sesión con contraseña incorrecta

**Requerimiento relacionado:**  
RF-01 / RF-10

**Objetivo:**  
Comprobar que una contraseña incorrecta no permita acceder.

**Datos utilizados:**

- Usuario: `admin`
- Contraseña: `321`

**Resultado esperado:**  
El sistema debe rechazar el acceso.

**Resultado inicial:**  
El sistema permitía ingresar.

**Resultado final:**  
La contraseña incorrecta es rechazada correctamente.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-003.

### CP-004 - Inicio de sesión con campos vacíos

**Requerimiento relacionado:**  
RF-01 / RF-09

**Objetivo:**  
Comprobar que no sea posible iniciar sesión dejando los campos vacíos.

**Resultado esperado:**  
El sistema debe solicitar el ingreso de usuario y contraseña.

**Resultado obtenido:**  
El sistema mostró correctamente un mensaje indicando que deben completarse los campos.

**Estado:**  
Aprobado.

### CP-005 - Registrar una obra válida

**Requerimiento relacionado:**  
RF-02

**Objetivo:**  
Comprobar que sea posible registrar una obra correctamente.

**Datos utilizados:**

- Nombre: `Obra Prueba 1`
- Descripción: `Obra utilizada para pruebas del sistema`

**Resultado esperado:**  
La obra debe guardarse y aparecer en el listado.

**Resultado obtenido:**  
La obra fue registrada correctamente.

**Estado:**  
Aprobado.

### CP-006 - Registrar una obra sin nombre

**Requerimiento relacionado:**  
RF-02 / RF-09

**Objetivo:**  
Comprobar que no se permita registrar una obra sin nombre.

**Resultado esperado:**  
El sistema debe impedir el registro y solicitar un nombre.

**Resultado obtenido:**  
El sistema mostró el mensaje correspondiente y no guardó la obra.

**Estado:**  
Aprobado.

### CP-007 - Registrar presupuesto válido

**Requerimiento relacionado:**  
RF-04 / RF-05

**Objetivo:**  
Comprobar el registro correcto de un presupuesto.

**Datos utilizados:**

- Obra: `Obra Prueba 1`
- Partida: `Materiales`
- Monto: `500000`

**Resultado esperado:**  
El presupuesto debe almacenarse y aparecer en la tabla.

**Resultado obtenido:**  
El presupuesto fue registrado correctamente.

**Estado:**  
Aprobado.

### CP-008 - Registrar presupuesto con monto igual a cero

**Requerimiento relacionado:**  
RF-04 / RF-09

**Objetivo:**  
Comprobar que no se acepten presupuestos con monto cero.

**Resultado esperado:**  
El sistema debe rechazar el monto e indicar que debe ser mayor que cero.

**Resultado final:**  
El valor es rechazado y se muestra un mensaje específico.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-004.

### CP-009 - Registrar presupuesto con monto negativo

**Requerimiento relacionado:**  
RF-04 / RF-09

**Objetivo:**  
Comprobar que no se acepten montos negativos.

**Resultado esperado:**  
El sistema debe rechazar el valor e indicar que el monto no puede ser negativo.

**Resultado final:**  
El monto negativo es rechazado con un mensaje específico.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-004.

### CP-010 - Registrar presupuesto con valor no numérico

**Requerimiento relacionado:**  
RF-04 / RF-09

**Datos utilizados:**

- Monto: `abc`

**Resultado esperado:**  
El sistema debe indicar que el monto debe ser un valor numérico.

**Resultado inicial:**  
El valor era rechazado, pero se mostraba un mensaje genérico.

**Resultado final:**  
El valor se rechaza y se muestra el mensaje correspondiente.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-004.

### CP-011 - Registrar gasto válido

**Requerimiento relacionado:**  
RF-06

**Objetivo:**  
Comprobar el registro correcto de un gasto.

**Datos utilizados:**

- Obra: `Obra Prueba 1`
- Partida: `Materiales`
- Concepto: `Compra de materiales`
- Monto: `200000`
- Fecha: `18-11-2026`

**Resultado esperado:**  
El gasto debe almacenarse y aparecer en la tabla.

**Resultado obtenido:**  
El gasto fue registrado correctamente.

**Estado:**  
Aprobado.

### CP-012 - Registrar gasto con monto negativo

**Requerimiento relacionado:**  
RF-06 / RF-09

**Resultado esperado:**  
El sistema debe impedir el registro e indicar que el monto no puede ser negativo.

**Resultado final:**  
El sistema rechaza correctamente el monto y muestra un mensaje específico.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-005.

### CP-013 - Registrar gasto con valor no numérico

**Requerimiento relacionado:**  
RF-06 / RF-09

**Datos utilizados:**

- Monto: `abc`

**Resultado esperado:**  
El sistema debe indicar que el monto debe ser un valor numérico.

**Resultado inicial:**  
El sistema rechazaba el valor, pero mostraba un mensaje genérico.

**Resultado final:**  
El valor es rechazado con el mensaje correspondiente.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-005.

### CP-014 - Registrar gasto con fecha inválida

**Requerimiento relacionado:**  
RF-06 / RF-09

**Objetivo:**  
Comprobar la validación de las fechas.

**Datos utilizados durante las pruebas:**

- `01012006`
- `31-02-2026`
- `01-01-0001`
- `18-11-2026`

**Resultado esperado:**

- Las fechas con formato incorrecto deben ser rechazadas.
- Las fechas inexistentes deben ser rechazadas.
- Las fechas fuera del rango permitido deben ser rechazadas.
- Las fechas válidas deben ser aceptadas.

**Resultado inicial:**  
El sistema permitió almacenar una fecha inválida.

**Resultado final:**

- `01012006` → rechazado.
- `31-02-2026` → rechazado.
- `01-01-0001` → rechazado.
- `18-11-2026` → aceptado.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-006.

### CP-015 - Comparación de costos

**Requerimiento relacionado:**  
RF-07

**Objetivo:**  
Comprobar el cálculo de presupuesto, gastos, diferencia y estado de cada obra.

**Escenarios comprobados:**

- Presupuesto mayor que gastos → **Superávit**.
- Presupuesto igual a gastos → **Equilibrado**.
- Gastos mayores que presupuesto → **Déficit**.

**Resultado esperado:**  
El sistema debe calcular correctamente la diferencia y mostrar el estado correspondiente.

**Resultado obtenido:**  
Los cálculos fueron correctos para los tres escenarios.

Posteriormente se mejoró la usabilidad del módulo incorporando un buscador por obra.

**Estado:**  
Aprobado después de corrección.

**Defecto de usabilidad relacionado:**  
DEF-007.

### CP-016 - Persistencia de datos

**Requerimiento relacionado:**  
RF-08 / RNF-05

**Objetivo:**  
Comprobar que los datos permanezcan almacenados después de cerrar y volver a abrir la aplicación.

**Datos comprobados:**

- Obras.
- Presupuestos.
- Gastos.
- Información utilizada en la comparación.

**Resultado esperado:**  
Los registros deben mantenerse almacenados.

**Resultado obtenido:**  
Los datos continuaron disponibles después de reiniciar la aplicación.

**Estado:**  
Aprobado.

### CP-017 - Ausencia de la base de datos original

**Requerimiento relacionado:**  
RF-09 / RNF-06

**Objetivo:**  
Comprobar el comportamiento del sistema cuando `sefel.db` no está disponible.

**Procedimiento:**  
Se renombró temporalmente la base de datos original antes de iniciar la aplicación.

**Resultado inicial:**  
SQLite creaba automáticamente una nueva base de datos vacía y la aplicación continuaba sin informar el problema.

**Corrección realizada:**  
Se agregó una comprobación de existencia de `sefel.db` antes de iniciar el sistema.

**Resultado final:**  
El sistema informa que la base de datos no está disponible, evita continuar y no crea silenciosamente una nueva base de datos vacía.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-008.

### CP-018 - Cerrar sesión

**Requerimiento relacionado:**  
RF-01 / RF-10

**Objetivo:**  
Comprobar que el usuario pueda cerrar correctamente la sesión.

**Resultado inicial:**  
La opción `Cerrar sesión` no realizaba ninguna acción.

**Resultado final:**  
Al cerrar sesión, la pantalla actual se elimina y el sistema vuelve al inicio de sesión. Para volver a acceder es necesario ingresar nuevamente credenciales válidas.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-009.

### CP-019 - Buscar una obra registrada

**Requerimiento relacionado:**  
RF-03 / RNF-01

**Objetivo:**  
Comprobar el funcionamiento del campo `Buscar obra`.

**Resultado inicial:**  
Era posible escribir en el campo, pero la tabla no se filtraba.

**Resultado final:**

- Permite buscar utilizando el nombre completo.
- Permite buscar utilizando parte del nombre.
- La tabla se actualiza mientras se escribe.
- Al dejar el campo vacío vuelven a mostrarse todas las obras.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-010.

### CP-020 - Acceder a los costos desde una obra

**Requerimiento relacionado:**  
RF-03 / RF-07

**Objetivo:**  
Comprobar el acceso desde una obra hacia su información de costos.

**Resultado inicial:**  
La interfaz mostraba `Ver costos`, pero no existía una acción funcional asociada.

**Resultado final:**  
Al hacer doble clic sobre una obra, el sistema abre el módulo de comparación de costos y deja seleccionada la obra consultada.

**Estado:**  
Aprobado después de corrección.

**Defecto relacionado:**  
DEF-011.

## 4. Resultado general

Los casos de prueba principales del prototipo fueron ejecutados.

Durante las pruebas se encontraron defectos de funcionalidad, seguridad, validación, recuperación y usabilidad.

Los defectos identificados dentro del alcance actual fueron corregidos y las funcionalidades afectadas fueron probadas nuevamente.

Después de las correcciones:

- El control de acceso funciona correctamente.
- Las obras, presupuestos y gastos se almacenan correctamente.
- Los montos inválidos son rechazados con mensajes específicos.
- Las fechas son validadas antes de registrar gastos.
- Los datos permanecen almacenados en SQLite.
- La ausencia de la base de datos es informada al usuario.
- El cierre de sesión funciona correctamente.
- La búsqueda de obras funciona.
- Es posible acceder desde una obra a su comparación de costos.
- El módulo de comparación permite buscar obras.
- Los cálculos de presupuesto, gastos y diferencia funcionan correctamente.

**Evidencias:**  
Las capturas y evidencias detalladas se mantienen en el documento Word utilizado para registrar la ejecución de las pruebas.

**Estado general:**  
Pruebas principales ejecutadas y correcciones verificadas.