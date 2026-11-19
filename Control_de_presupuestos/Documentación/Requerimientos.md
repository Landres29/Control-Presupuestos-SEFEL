# Requerimientos del sistema

## 1. Objetivo

Definir las funciones principales que debe cumplir el prototipo de Control de Presupuestos SEFEL.

Estos requerimientos serán utilizados como base para el desarrollo, las pruebas y la identificación de errores o defectos del sistema.

---

# 2. Requerimientos funcionales

## RF-01 - Inicio de sesión

El sistema debe permitir que un usuario ingrese mediante un nombre de usuario y una contraseña.

### Debe permitir

- Ingresar usuario.
- Ingresar contraseña.
- Validar las credenciales.
- Permitir el acceso cuando las credenciales sean correctas.
- Mostrar un mensaje cuando las credenciales sean incorrectas.

### No debe permitir

- Ingresar al sistema con un usuario inexistente.
- Ingresar con una contraseña incorrecta.
- Ingresar dejando campos obligatorios vacíos.

### Estado

En desarrollo.

El inicio de sesión ya cuenta con una interfaz inicial, pero todavía se deben mejorar las validaciones y controles de seguridad.

---

## RF-02 - Registro de obras

El sistema debe permitir registrar nuevas obras.

### Datos mínimos

- Nombre de la obra.
- Descripción.

### Debe permitir

- Registrar una nueva obra.
- Guardar la información en la base de datos.
- Mostrar la obra registrada en la pantalla principal.
- Consultar las obras existentes.

### No debe permitir

- Registrar una obra sin nombre.

### Estado

Implementado.

---

## RF-03 - Consulta de obras

El sistema debe mostrar las obras registradas.

### Debe permitir

- Visualizar las obras almacenadas.
- Identificar el nombre de cada obra.
- Seleccionar una obra para trabajar con sus presupuestos y gastos.

### Estado

Implementado.

---

## RF-04 - Registro de presupuestos

El sistema debe permitir registrar montos presupuestados asociados a una obra.

### Datos mínimos

- Obra.
- Partida.
- Monto presupuestado.

### Debe permitir

- Seleccionar una obra existente.
- Registrar una partida.
- Ingresar un monto presupuestado.
- Guardar el presupuesto en la base de datos.
- Consultar los presupuestos registrados.

### No debe permitir

- Registrar un presupuesto sin seleccionar una obra.
- Registrar una partida vacía.
- Registrar un monto vacío.
- Registrar texto en un campo que requiere un valor numérico.
- Registrar un monto igual o menor que cero.

### Estado

Implementado parcialmente.

Las funciones principales se encuentran implementadas, pero las validaciones serán revisadas durante las pruebas.

---

## RF-05 - Registro de partidas

El sistema debe permitir utilizar partidas para organizar los presupuestos y gastos.

### Debe permitir

- Registrar o indicar una partida.
- Asociar una partida a un presupuesto.
- Asociar una partida a un gasto.
- Utilizar la partida como referencia para comparar costos.

### No debe permitir

- Utilizar una partida vacía.

### Estado

Implementado de forma básica.

---

## RF-06 - Registro de gastos

El sistema debe permitir registrar gastos reales asociados a una obra.

### Datos mínimos

- Obra.
- Partida.
- Concepto.
- Monto.
- Fecha.

### Debe permitir

- Seleccionar una obra.
- Indicar la partida correspondiente.
- Registrar el concepto del gasto.
- Registrar el monto.
- Registrar la fecha.
- Guardar el gasto en SQLite.
- Consultar los gastos registrados.

### No debe permitir

- Registrar un gasto sin seleccionar una obra.
- Registrar una partida vacía.
- Registrar un concepto vacío.
- Registrar un monto vacío.
- Registrar un monto no numérico.
- Registrar un monto igual o menor que cero.
- Registrar una fecha vacía.

### Estado

Implementado parcialmente.

Las validaciones específicas de fecha y caracteres serán comprobadas durante las pruebas.

---

## RF-07 - Comparación de costos

El sistema debe permitir comparar los montos presupuestados con los gastos reales de una obra.

### Debe mostrar

- Obra.
- Presupuesto total.
- Gastos totales.
- Diferencia.
- Estado.

### Cálculo

La diferencia se obtiene mediante:

**Diferencia = Presupuesto - Gastos**

### Resultado esperado

- Si la diferencia es mayor que cero, existe un superávit.
- Si la diferencia es menor que cero, existe un déficit.
- Si la diferencia es igual a cero, existe equilibrio.

### Debe permitir

- Obtener los valores desde la base de datos.
- Calcular automáticamente los totales.
- Mostrar el resultado de la comparación.

### Estado

Implementado.

Será revisado mediante casos de prueba para comprobar que los cálculos sean correctos.

---

## RF-08 - Persistencia de datos

El sistema debe mantener almacenada la información después de cerrar y volver a ejecutar la aplicación.

### Información considerada

- Obras.
- Presupuestos.
- Gastos.

### Debe permitir

- Cerrar la aplicación.
- Volver a ejecutar el programa.
- Consultar los registros creados anteriormente.

### Estado

Implementado mediante SQLite.

---

## RF-09 - Manejo de errores

El sistema debe informar al usuario cuando una operación no pueda realizarse correctamente.

### Debe permitir

- Mostrar mensajes cuando falten datos obligatorios.
- Mostrar mensajes cuando un dato tenga un formato incorrecto.
- Evitar que el programa se cierre de forma inesperada por errores de entrada.
- Informar cuando una operación no pueda completarse.

### Estado

En desarrollo.

Se mejorará de acuerdo con los errores identificados durante las pruebas.

---

## RF-10 - Control de acceso

El sistema debe controlar qué usuarios pueden ingresar a la aplicación.

### Debe permitir

- Utilizar usuarios previamente definidos.
- Validar usuario y contraseña.
- Rechazar usuarios inexistentes.
- Rechazar contraseñas incorrectas.
- Registrar o controlar intentos incorrectos de acceso.

### Requisito de seguridad propuesto

Después de varios intentos incorrectos consecutivos, el sistema deberá aplicar una medida de control para evitar intentos ilimitados.

La implementación exacta será definida durante el desarrollo del Sprint 4.

### Estado

Pendiente de completar.

---

# 3. Requerimientos no funcionales

## RNF-01 - Usabilidad

La aplicación debe utilizar una interfaz simple y comprensible.

El usuario debe poder identificar fácilmente las principales funciones:

- Obras.
- Presupuestos.
- Gastos.
- Comparación de costos.

---

## RNF-02 - Integridad

El sistema debe evitar modificaciones incorrectas o registros inválidos que puedan afectar los datos almacenados.

Las validaciones deben ayudar a mantener la información de presupuestos y gastos de forma correcta.

---

## RNF-03 - Confidencialidad

El acceso a la información del sistema debe estar limitado a usuarios autorizados mediante el inicio de sesión.

---

## RNF-04 - Disponibilidad

La aplicación y la información almacenada deben estar disponibles mientras el equipo y la base de datos local funcionen correctamente.

---

## RNF-05 - Persistencia

La información debe almacenarse en una base de datos SQLite y permanecer disponible después de cerrar la aplicación.

---

## RNF-06 - Manejo de fallos

El sistema debe mostrar mensajes comprensibles cuando ocurra un problema y evitar, cuando sea posible, que la aplicación se cierre inesperadamente.

---

# 4. Reglas generales de validación

Las reglas específicas serán comprobadas mediante los casos de prueba.

Como base se consideran las siguientes:

- Los campos obligatorios no pueden estar vacíos.
- Los montos deben aceptar únicamente valores numéricos válidos.
- Los montos deben ser mayores que cero.
- Una obra debe existir antes de asociarle presupuestos o gastos.
- Las fechas deberán utilizar un formato válido definido por el sistema.
- Los campos de texto deberán aceptar únicamente los caracteres establecidos para cada tipo de dato.
- Los mensajes de error deben explicar de forma comprensible por qué una operación fue rechazada.

---

# 5. Alcance actual

El prototipo se concentra en las funciones principales relacionadas con:

- Inicio de sesión.
- Registro y consulta de obras.
- Registro de presupuestos.
- Uso de partidas.
- Registro de gastos.
- Comparación de costos.
- Persistencia de información.
- Validaciones y seguridad básica.

Funciones más complejas como alertas automáticas, importación masiva de información y funciones avanzadas de gestión quedan fuera del alcance actual del prototipo.

---

# 6. Relación con los Sprints

Los requerimientos se distribuyen de la siguiente forma:

### Sprint 1

- RF-01 Inicio de sesión.
- RF-02 Registro de obras.
- RF-03 Consulta de obras.
- RF-08 Persistencia de datos.

### Sprint 2

- RF-04 Registro de presupuestos.
- RF-05 Registro de partidas.

### Sprint 3

- RF-06 Registro de gastos.

### Sprint 4

- RF-07 Comparación de costos.
- RF-09 Manejo de errores.
- RF-10 Control de acceso.
- Requerimientos no funcionales relacionados con seguridad, integridad, disponibilidad y usabilidad.
- Ejecución de pruebas y corrección de defectos.

---

# 7. Estado general

Los requerimientos principales del prototipo se encuentran implementados de forma inicial.

Durante el Sprint 4 se revisarán las validaciones, seguridad, manejo de errores y comportamiento del sistema mediante casos de prueba.

Los defectos encontrados serán registrados y corregidos antes de finalizar el prototipo.