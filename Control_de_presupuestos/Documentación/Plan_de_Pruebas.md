# Plan de Pruebas del Sistema

## 1. Objetivo

El objetivo de este plan de pruebas es verificar que el prototipo de **Control de Presupuestos SEFEL** funcione correctamente de acuerdo con los requerimientos definidos.

Las pruebas permiten identificar errores o defectos, comprobar las funciones principales del sistema, registrar los resultados obtenidos y verificar las correcciones realizadas.

## 2. Alcance

Las pruebas se realizan sobre las principales funcionalidades del prototipo.

### Funcionalidades incluidas

- Inicio de sesión.
- Registro de obras.
- Consulta de obras.
- Búsqueda de obras.
- Registro de presupuestos.
- Registro de partidas.
- Registro de gastos.
- Consulta de gastos.
- Comparación de costos.
- Consulta de costos desde una obra.
- Persistencia de datos.
- Validación de datos ingresados.
- Manejo de errores.
- Manejo de ausencia de la base de datos.
- Cierre de sesión.
- Control de acceso.
- Seguridad básica.
- Usabilidad.

### Funcionalidades fuera del alcance

- Pruebas de carga.
- Pruebas de estrés.
- Pruebas avanzadas de rendimiento.
- Pruebas de compatibilidad con múltiples sistemas operativos.
- Funciones que no forman parte del prototipo actual.
- Bloqueo temporal automático después de varios intentos fallidos de inicio de sesión.
- Gestión avanzada de usuarios y permisos.

## 3. Estrategia de pruebas

La estrategia principal utilizada es la **prueba de caja negra**.

### 3.1 Caja negra

Las pruebas de caja negra comprueban el comportamiento del sistema desde el punto de vista del usuario.

Se utilizan datos válidos e inválidos para verificar la respuesta de la aplicación.

**Ejemplos:**

- Usuario y contraseña correctos.
- Usuario inexistente.
- Contraseña incorrecta.
- Campos vacíos.
- Montos válidos.
- Montos iguales a cero.
- Montos negativos.
- Valores no numéricos.
- Fechas válidas.
- Fechas con formato incorrecto.
- Fechas inexistentes.
- Datos que no deberían ser aceptados.

No es necesario conocer el funcionamiento interno del código para ejecutar estas pruebas.

### 3.2 Caja blanca

Se consideran revisiones de caja blanca en algunas funciones internas del sistema.

Se utilizan principalmente para revisar:

- Registro de información.
- Cálculos de presupuesto.
- Cálculos de gastos.
- Cálculo de diferencias.
- Funciones de acceso a SQLite.
- Validaciones internas.
- Comprobación de existencia de la base de datos.

Estas revisiones son realizadas por los desarrolladores.

## 4. Niveles de prueba

### 4.1 Pruebas unitarias

Se utilizan para revisar funciones o validaciones específicas del sistema.

**Ejemplos:**

- Registro de obra.
- Registro de presupuesto.
- Registro de gasto.
- Obtención de totales.
- Cálculo de diferencias.
- Validación de montos.
- Validación de fechas.

### 4.2 Pruebas de integración

Comprueban que los diferentes componentes funcionen correctamente en conjunto.

**Ejemplos:**

- Interfaz de obras con SQLite.
- Presupuestos asociados a una obra.
- Gastos asociados a una obra.
- Comparación utilizando presupuestos y gastos almacenados.
- Navegación entre las diferentes pantallas.
- Consulta de costos desde una obra.
- Inicio y cierre de sesión.

### 4.3 Pruebas de sistema

Se prueba el prototipo completo desde la perspectiva del usuario.

**Flujo principal considerado:**

1. Iniciar sesión.
2. Registrar o consultar una obra.
3. Registrar un presupuesto.
4. Registrar un gasto.
5. Consultar la información.
6. Comparar los costos.
7. Buscar una obra.
8. Acceder a los costos desde una obra.
9. Cerrar sesión.

### 4.4 Prueba de aceptación

La prueba de aceptación deberá ser realizada por un usuario o representante correspondiente.

Su objetivo es comprobar si el prototipo cumple con las funciones principales esperadas desde el punto de vista del usuario final.

Esta prueba es independiente de las pruebas realizadas por el equipo de desarrollo.

## 5. Tipos de pruebas

### 5.1 Pruebas funcionales

Se comprueba que cada funcionalidad cumpla con el comportamiento definido en los requerimientos.

### 5.2 Pruebas de seguridad

Se revisan principalmente:

- Validación de usuario y contraseña.
- Rechazo de usuarios inexistentes.
- Rechazo de contraseñas incorrectas.
- Campos obligatorios del inicio de sesión.
- Control de acceso.
- Cierre de sesión.
- Protección básica de la información.
- Confidencialidad.
- Integridad.
- Disponibilidad.

**Mejora futura:**  
El bloqueo temporal después de varios intentos fallidos se considera una mejora futura y no forma parte del alcance de la versión actual.

### 5.3 Pruebas de usabilidad

Se comprueba que:

- Los botones y opciones sean comprensibles.
- Los mensajes sean claros.
- Las pantallas sean fáciles de utilizar.
- La navegación sea simple.
- Los campos sean fáciles de identificar.
- Las opciones visibles tengan una funcionalidad asociada.
- La búsqueda facilite la consulta de información.

### 5.4 Pruebas de recuperación

Se comprueba que el sistema pueda manejar determinados fallos sin generar pérdida innecesaria de información.

Se consideran:

- Cerrar y volver a abrir la aplicación.
- Comprobar que los registros continúen disponibles.
- Comprobar la persistencia en SQLite.
- Comprobar el comportamiento cuando la base de datos original no se encuentra disponible.
- Mostrar un mensaje al usuario cuando la aplicación no pueda acceder a la base de datos necesaria.

### 5.5 Pruebas de regresión

Después de corregir un defecto se vuelve a ejecutar la funcionalidad afectada.

También se comprueba que la modificación no haya afectado otras funciones relacionadas.

**Ejemplos realizados:**

- Repetición de pruebas del inicio de sesión después de corregir la validación de credenciales.
- Repetición de pruebas de fechas después de incorporar su validación.
- Repetición de pruebas de montos después de mejorar sus mensajes.
- Comprobación del cierre de sesión después de implementarlo.
- Comprobación del buscador después de incorporar el filtrado.
- Comprobación de la comparación de costos después de implementar el acceso desde Obras.

## 6. Ambiente de pruebas

Las pruebas se realizan en el mismo ambiente utilizado para desarrollar el prototipo.

### Software

- Windows 10 o Windows 11.
- Python.
- Tkinter.
- SQLite.
- Visual Studio Code.
- Git.
- GitHub.

### Hardware

Se utilizan los computadores disponibles para el desarrollo y las pruebas del proyecto.

No se requiere hardware especializado.

## 7. Datos de prueba

Se utilizan datos válidos e inválidos para comprobar el comportamiento del sistema.

### Ejemplos de datos válidos

- Nombre de obra correctamente ingresado.
- Montos numéricos mayores que cero.
- Fechas válidas con formato `DD-MM-AAAA`.
- Usuario válido.
- Contraseña correcta.

### Ejemplos de datos inválidos

- Campos vacíos.
- Montos negativos.
- Monto igual a cero.
- Letras en campos numéricos.
- Usuario inexistente.
- Contraseña incorrecta.
- Fechas con formato incorrecto.
- Fechas inexistentes.
- Fechas fuera del rango establecido.

**Ejemplos:**

- `01012006`
- `31-02-2026`
- `01-01-0001`

Estos valores permiten comprobar tanto el formato como la validez del dato ingresado.

## 8. Caracteres y valores permitidos

Los datos permitidos dependen del tipo de campo.

No se utiliza una única regla para todos los campos.

### Nombre de obra

Puede aceptar:

- Letras.
- Números.
- Espacios.
- Caracteres utilizados habitualmente en nombres.

El nombre no puede quedar vacío.

### Partida

Debe contener información que permita identificar la partida correspondiente.

No puede quedar vacía al realizar un registro.

### Concepto o descripción

Puede aceptar:

- Letras.
- Números.
- Espacios.
- Caracteres especiales necesarios para escribir una descripción.

### Monto

Debe aceptar únicamente valores numéricos mayores que cero.

Se consideran inválidos:

- Campo vacío.
- Cero.
- Valores negativos.
- Valores no numéricos.

### Fecha

Para el registro de gastos se utiliza el formato:

`DD-MM-AAAA`

La fecha debe:

- Cumplir con el formato definido.
- Corresponder a una fecha real.
- Utilizar un año dentro del rango permitido por el sistema.

### Usuario y contraseña

El prototipo valida las credenciales utilizadas para el acceso.

Las credenciales incorrectas deben ser rechazadas.

## 9. Responsables

El equipo de desarrollo es responsable de:

- Preparar los casos de prueba.
- Ejecutar las pruebas.
- Registrar los resultados.
- Identificar defectos.
- Clasificar los defectos.
- Corregir errores.
- Repetir las pruebas después de las correcciones.
- Mantener las evidencias.
- Registrar los cambios mediante Git y GitHub.

La prueba de aceptación corresponde a un usuario o representante.

## 10. Registro de resultados

Cada caso de prueba registra, según corresponda:

- Identificador.
- Funcionalidad.
- Requerimiento relacionado.
- Datos de entrada.
- Pasos realizados.
- Resultado esperado.
- Resultado obtenido.
- Estado.
- Defecto relacionado.

### Estados utilizados

- **Aprobado.**
- **Fallido.**
- **Pendiente.**
- **Aprobado después de corrección.**

Si una prueba falla, se registra el defecto correspondiente en `Registro_de_defectos.md`.

Las evidencias detalladas de ejecución se mantienen en un documento Word con sus respectivas capturas.

## 11. Clasificación de severidad

Los defectos encontrados se clasifican según su impacto.

### Crítico

Defecto que impide utilizar una función principal o compromete seriamente la seguridad o integridad de los datos.

**Ejemplos:**

- El sistema no inicia.
- Se pierden registros almacenados.
- Se puede ingresar sin credenciales válidas.
- Un cálculo principal entrega resultados incorrectos.

### Alto

Defecto importante que afecta una funcionalidad principal, pero permite continuar utilizando otras partes del sistema.

**Ejemplos:**

- No se puede registrar un gasto.
- Un presupuesto no queda asociado a la obra correspondiente.
- Una validación importante no funciona.

### Medio

Defecto que afecta parcialmente una función o el manejo de una situación, pero permite continuar trabajando en otras partes del sistema.

**Ejemplos:**

- Una fecha inválida es aceptada.
- Una función visible no realiza la acción esperada.
- El sistema no maneja correctamente la ausencia de la base de datos.
- Una búsqueda no funciona.

### Bajo

Defecto que no impide el funcionamiento principal y se relaciona principalmente con usabilidad o presentación.

**Ejemplos:**

- Mensaje poco específico.
- Elemento visual poco intuitivo.
- Problema menor de presentación.
- Falta de una ayuda de consulta secundaria.

## 12. Criterios de entrada

Una funcionalidad puede comenzar a probarse cuando:

- Se encuentre implementada.
- La aplicación pueda ejecutarse.
- La base de datos se encuentre disponible para las pruebas normales.
- Existan datos de prueba preparados.
- El requerimiento correspondiente se encuentre definido.

## 13. Criterios de salida

La etapa principal de pruebas puede considerarse finalizada cuando:

- Los casos de prueba principales hayan sido ejecutados.
- Las funcionalidades principales se encuentren operativas.
- No existan defectos críticos pendientes.
- Los defectos incluidos en el alcance hayan sido corregidos o justificados.
- Las correcciones hayan sido verificadas.
- Los resultados se encuentren documentados.
- Las evidencias necesarias se encuentren disponibles.
- Los cambios se encuentren registrados mediante control de versiones.

**Resultado actual:**  
Estos criterios se cumplen para la etapa de pruebas realizada por el equipo de desarrollo.

La prueba de aceptación puede realizarse posteriormente por el usuario o representante correspondiente.

## 14. Gestión de defectos

Cuando se detecta un defecto:

1. Se registra en `Registro_de_defectos.md`.
2. Se relaciona con el caso de prueba correspondiente.
3. Se asigna una severidad.
4. Se analiza el problema.
5. Se realiza la corrección cuando corresponde.
6. La modificación se registra mediante Git y GitHub.
7. Se vuelve a ejecutar la prueba afectada.
8. Si el resultado es correcto, el defecto se marca como corregido.

## 15. Riesgos de las pruebas

Se consideran los siguientes riesgos:

- Tiempo limitado para ejecutar todos los casos.
- Cambios realizados durante el Sprint 4.
- Errores durante la integración de módulos.
- Pérdida accidental de información de prueba.
- Falta de disponibilidad del usuario para realizar la prueba de aceptación.
- Correcciones que puedan generar nuevos errores.

### Medidas utilizadas para reducir los riesgos

- Control de versiones mediante Git y GitHub.
- Copias de seguridad cuando se realizan pruebas sobre la base de datos.
- Repetición de pruebas después de cambios importantes.
- Registro de defectos y correcciones.

## 16. Relación con los requerimientos

Los casos de prueba se relacionan con los requerimientos definidos en `Requerimientos.md`.

Esto permite mantener trazabilidad entre:

**Requerimiento → Caso de prueba → Resultado → Defecto → Corrección**

Esta relación permite demostrar:

- Qué funcionalidad fue probada.
- Qué resultado se obtuvo.
- Qué problema fue encontrado.
- Qué corrección se realizó.
- Si la corrección funcionó posteriormente.

## 17. Resultado de la ejecución

Durante el Sprint 4 se ejecutaron los casos de prueba principales del prototipo.

Las pruebas permitieron detectar defectos relacionados con:

- Validación del inicio de sesión.
- Mensajes de validación.
- Validación de fechas.
- Usabilidad.
- Manejo de fallos.
- Cierre de sesión.
- Búsqueda de información.
- Consulta de costos.

Los defectos considerados dentro del alcance actual fueron corregidos y las funcionalidades afectadas fueron verificadas nuevamente.

**Resultado:**  
No existen defectos críticos pendientes dentro de los casos ejecutados.

## 18. Estado del plan

**Plan de pruebas definido y ejecutado para las funcionalidades principales del prototipo.**

Los resultados y defectos se encuentran documentados.

Las evidencias de ejecución se mantienen mediante capturas, documentación y control de versiones.

La prueba de aceptación por parte de un usuario o representante queda como actividad independiente cuando corresponda.