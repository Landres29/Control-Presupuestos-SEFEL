# Plan de Pruebas del Sistema

## 1. Objetivo

El objetivo de este plan de pruebas es verificar que el prototipo de Control de Presupuestos SEFEL funcione correctamente de acuerdo con los requerimientos definidos.

Las pruebas permitirán identificar errores o defectos antes de finalizar el desarrollo, comprobar las funciones principales del sistema y registrar las correcciones realizadas.

---

# 2. Alcance

Las pruebas se realizarán sobre las principales funcionalidades del prototipo.

Se incluirán:

- Inicio de sesión.
- Registro de obras.
- Consulta de obras.
- Registro de presupuestos.
- Registro de partidas.
- Registro de gastos.
- Consulta de gastos.
- Comparación de costos.
- Persistencia de datos.
- Validación de datos ingresados.
- Manejo de errores.
- Control de acceso.
- Seguridad básica.
- Usabilidad.

Quedan fuera del alcance:

- Pruebas de carga.
- Pruebas de estrés.
- Pruebas de rendimiento avanzadas.
- Pruebas de compatibilidad con múltiples sistemas operativos.
- Pruebas de funciones que no forman parte del prototipo actual.

---

# 3. Estrategia de pruebas

La estrategia principal será la prueba de caja negra.

## 3.1 Caja negra

Las pruebas de caja negra verificarán el comportamiento del sistema desde el punto de vista del usuario.

Se ingresarán datos válidos e inválidos para comprobar si el sistema responde correctamente.

Ejemplos:

- Usuario y contraseña correctos.
- Usuario inexistente.
- Contraseña incorrecta.
- Campos vacíos.
- Montos válidos e inválidos.
- Fechas válidas e inválidas.
- Datos que no deberían ser aceptados.

No será necesario conocer el funcionamiento interno del código para ejecutar estas pruebas.

## 3.2 Caja blanca

Se podrán realizar pruebas de caja blanca en algunas funciones internas del sistema.

Se utilizarán principalmente para revisar:

- Cálculos de presupuesto.
- Cálculos de gastos.
- Cálculo de diferencias.
- Funciones de acceso a la base de datos.
- Validaciones internas.

Estas pruebas serán realizadas por los desarrolladores.

## 3.3 Caja gris

Las pruebas de caja gris se utilizarán cuando sea necesario verificar la relación entre la interfaz y la base de datos.

Ejemplos:

- Registrar una obra desde la interfaz y verificar su almacenamiento en SQLite.
- Registrar un gasto y comprobar que quede asociado a la obra correcta.
- Verificar que la comparación utilice los datos almacenados en la base de datos.

---

# 4. Niveles de prueba

## 4.1 Pruebas unitarias

Se utilizarán para revisar funciones específicas del sistema.

Ejemplos:

- Función de registro de obra.
- Función de registro de presupuesto.
- Función de registro de gasto.
- Función que obtiene los totales.
- Función que calcula la diferencia de costos.

## 4.2 Pruebas de integración

Se utilizarán para comprobar que los diferentes componentes funcionen correctamente en conjunto.

Ejemplos:

- Interfaz de obras con SQLite.
- Presupuestos asociados a una obra.
- Gastos asociados a una obra.
- Comparación utilizando presupuestos y gastos registrados.

## 4.3 Pruebas de sistema

Se probará el prototipo completo desde la perspectiva del usuario.

Se verificará que sea posible realizar el flujo principal:

1. Iniciar sesión.
2. Registrar una obra.
3. Registrar un presupuesto.
4. Registrar un gasto.
5. Consultar los datos.
6. Comparar los costos.

## 4.4 Prueba de aceptación

La prueba de aceptación deberá ser realizada por un usuario o representante correspondiente.

Su objetivo será comprobar si el prototipo cumple con las funciones principales esperadas.

---

# 5. Tipos de pruebas

## 5.1 Pruebas funcionales

Se comprobará que cada funcionalidad cumpla con el comportamiento definido en los requerimientos.

## 5.2 Pruebas de seguridad

Se revisarán principalmente:

- Validación de usuario y contraseña.
- Rechazo de usuarios inexistentes.
- Rechazo de contraseñas incorrectas.
- Control de intentos incorrectos de acceso.
- Protección básica de la información.
- Confidencialidad.
- Integridad.
- Disponibilidad.

## 5.3 Pruebas de usabilidad

Se comprobará que:

- Los botones sean comprensibles.
- Los mensajes sean claros.
- Las pantallas sean fáciles de utilizar.
- La navegación sea simple.
- Los campos sean fáciles de identificar.

## 5.4 Pruebas de recuperación

Cuando corresponda, se verificará que el sistema pueda manejar fallos sin perder innecesariamente la información.

Ejemplos:

- Cerrar y volver a abrir la aplicación.
- Comprobar que los registros continúen disponibles.
- Manejar un problema de acceso a la base de datos mostrando un mensaje al usuario.

## 5.5 Pruebas de regresión

Después de corregir un defecto, se volverá a probar la funcionalidad afectada.

También se comprobará que la corrección no haya provocado problemas en otras funciones del sistema.

---

# 6. Ambiente de pruebas

Las pruebas se realizarán en el mismo ambiente utilizado para desarrollar el prototipo.

## Software

- Windows 10 o Windows 11.
- Python.
- Tkinter.
- SQLite.
- Visual Studio Code.
- Git.
- GitHub.

## Hardware

Se utilizarán los computadores disponibles para el desarrollo y las pruebas del proyecto.

No se requiere hardware especializado.

---

# 7. Datos de prueba

Se utilizarán datos válidos e inválidos para comprobar el comportamiento del sistema.

## Ejemplos de datos válidos

- Nombre de obra correctamente ingresado.
- Montos numéricos mayores que cero.
- Fechas válidas.
- Usuarios registrados.
- Contraseñas correctas.

## Ejemplos de datos inválidos

- Campos vacíos.
- Montos negativos.
- Monto igual a cero.
- Letras en campos numéricos.
- Usuario inexistente.
- Contraseña incorrecta.
- Fechas con formato incorrecto.
- Fechas con formato válido pero valor no aceptable.

Ejemplo:

`01-01-0001`

Este dato puede tener una estructura similar a una fecha correcta, pero deberá comprobarse si cumple con las reglas definidas por el sistema.

---

# 8. Caracteres permitidos

Los caracteres permitidos se definirán según el tipo de campo.

No se aplicará una única regla para todos los campos.

Por ejemplo:

## Nombre de obra

Podrá aceptar:

- Letras.
- Números.
- Espacios.
- Algunos caracteres utilizados habitualmente en nombres.

## Concepto o descripción

Podrá aceptar:

- Letras.
- Números.
- Espacios.
- Caracteres especiales necesarios para escribir descripciones.

## Monto

Deberá aceptar únicamente valores numéricos válidos.

## Usuario

Los caracteres permitidos serán definidos al implementar completamente el control de acceso.

Las reglas definitivas deberán quedar registradas en los casos de prueba.

---

# 9. Responsables

El equipo de desarrollo será responsable de:

- Preparar los casos de prueba.
- Ejecutar las pruebas.
- Registrar los resultados.
- Identificar defectos.
- Corregir errores.
- Repetir las pruebas después de las correcciones.

La prueba de aceptación deberá ser realizada por un usuario o representante correspondiente.

---

# 10. Registro de resultados

Cada caso de prueba deberá registrar como mínimo:

- Identificador.
- Funcionalidad.
- Requerimiento relacionado.
- Datos de entrada.
- Pasos realizados.
- Resultado esperado.
- Resultado obtenido.
- Estado de la prueba.

Los posibles estados serán:

- Aprobado.
- Fallido.
- Pendiente.

Si una prueba falla, se deberá registrar el defecto correspondiente en `Registro_de_defectos.md`.

---

# 11. Clasificación de severidad

Los defectos encontrados serán clasificados según su impacto.

## Crítico

Defecto que impide utilizar una función principal o compromete seriamente la seguridad o integridad de los datos.

Ejemplos:

- El sistema no inicia.
- Se pierden los registros almacenados.
- Se puede ingresar sin credenciales válidas.
- Un cálculo principal entrega resultados incorrectos.

## Alto

Defecto importante que afecta una funcionalidad principal, pero permite continuar utilizando otras partes del sistema.

Ejemplos:

- No se puede registrar un gasto.
- Un presupuesto no queda asociado a la obra correcta.
- Una validación importante no funciona.

## Medio

Defecto que afecta parcialmente una función, pero existe una forma de continuar trabajando.

Ejemplos:

- Mensaje poco claro.
- Validación secundaria incorrecta.
- Un dato se muestra de forma incorrecta sin afectar el almacenamiento.

## Bajo

Defecto que no afecta el funcionamiento principal.

Ejemplos:

- Error de texto.
- Elemento visual mal alineado.
- Color o tamaño poco adecuado.
- Problema menor de presentación.

---

# 12. Criterios de entrada

Una funcionalidad podrá comenzar a probarse cuando:

- Se encuentre implementada.
- La aplicación pueda ejecutarse.
- La base de datos se encuentre disponible.
- Existan datos de prueba preparados.
- El requerimiento correspondiente se encuentre definido.

---

# 13. Criterios de salida

La etapa de pruebas podrá considerarse finalizada cuando:

- Los casos de prueba principales hayan sido ejecutados.
- Las funcionalidades principales se encuentren operativas.
- No existan defectos críticos pendientes.
- Los defectos altos importantes hayan sido corregidos o justificados.
- Las correcciones hayan sido sometidas a pruebas de regresión.
- Los resultados se encuentren documentados.
- Las evidencias necesarias se encuentren disponibles.

---

# 14. Gestión de defectos

Cuando se encuentre un defecto:

1. Se registrará en `Registro_de_defectos.md`.
2. Se asignará una severidad.
3. Se analizará la causa.
4. Se realizará una corrección cuando corresponda.
5. La modificación quedará registrada mediante Git y GitHub.
6. Se volverá a ejecutar el caso de prueba.
7. Si la prueba resulta correcta, el defecto podrá marcarse como corregido.

---

# 15. Riesgos de las pruebas

Se consideran los siguientes riesgos:

- Tiempo limitado para ejecutar todos los casos.
- Cambios realizados durante el Sprint 4.
- Errores que aparezcan durante la integración de módulos.
- Pérdida accidental de información de prueba.
- Falta de disponibilidad del usuario para realizar la prueba de aceptación.
- Correcciones que puedan generar nuevos errores.

Para reducir estos riesgos se utilizará control de versiones mediante GitHub y se realizarán pruebas de regresión después de cambios importantes.

---

# 16. Relación con los requerimientos

Los casos de prueba serán relacionados con los requerimientos definidos en `Requerimientos.md`.

Esto permitirá mantener trazabilidad entre:

**Requerimiento → Caso de prueba → Resultado → Defecto → Corrección**

Esta relación permitirá demostrar qué se probó, qué errores fueron encontrados y qué modificaciones fueron realizadas durante el desarrollo.

---

# 17. Estado del plan

Plan de pruebas definido.

La ejecución de los casos de prueba se realizará durante el Sprint 4.