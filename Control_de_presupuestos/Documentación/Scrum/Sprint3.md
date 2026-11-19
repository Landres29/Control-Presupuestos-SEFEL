# Sprint 3 - Registro de gastos asociados a obras y partidas

## Objetivo

Implementar el módulo de gastos del sistema, permitiendo registrar gastos reales asociados a una obra y a una partida, de manera que posteriormente puedan ser utilizados para comparar los costos presupuestados con los costos reales.

## Actividades

Durante este Sprint se consideran las siguientes actividades:

- Implementar el registro de gastos.
- Asociar cada gasto a una obra existente.
- Asociar cada gasto a una partida.
- Registrar el concepto del gasto.
- Registrar el monto del gasto.
- Registrar la fecha del gasto.
- Mostrar los gastos registrados en una tabla.
- Guardar la información utilizando la base de datos SQLite.
- Verificar que los gastos permanezcan almacenados después de cerrar y volver a abrir la aplicación.

## Responsable

Desarrollador.

## Duración estimada

1 semana.

## Entregable

Módulo de gastos.

## Funcionalidades implementadas

### Registro de gastos

El sistema permite registrar un gasto real asociado a una obra previamente creada.

Para registrar un gasto se consideran los siguientes datos:

- Obra.
- Partida.
- Concepto.
- Monto.
- Fecha.

### Asociación con obras

Cada gasto se relaciona con una obra existente mediante la base de datos.

Esto permite identificar a qué obra corresponde cada gasto registrado.

### Asociación con partidas

El gasto se registra indicando la partida correspondiente, permitiendo mantener una relación entre los costos presupuestados y los costos reales.

### Consulta de gastos

Los gastos registrados se muestran en una tabla para facilitar su consulta.

La tabla permite visualizar:

- Obra.
- Partida.
- Concepto.
- Monto.
- Fecha.

### Persistencia de datos

Los gastos se almacenan en SQLite.

La información debe permanecer disponible después de cerrar y volver a ejecutar la aplicación.

## Validaciones iniciales

Durante el registro de gastos se consideran las siguientes validaciones básicas:

- Se debe seleccionar una obra.
- La partida no puede estar vacía.
- El concepto no puede estar vacío.
- El monto no puede estar vacío.
- El monto debe contener un valor numérico.
- El monto debe ser mayor que cero.
- La fecha no puede estar vacía.

Las validaciones específicas relacionadas con formato de fechas, caracteres permitidos y casos inválidos se definirán posteriormente en los requerimientos y casos de prueba.

## Control de versiones

Los cambios desarrollados durante este Sprint se registran mediante Git y GitHub.

Los commits correspondientes permiten demostrar la incorporación del módulo de gastos y su conexión con la base de datos.

## Revisión del Sprint

Al finalizar el Sprint se debe comprobar:

- Que las obras existentes aparezcan en el selector de gastos.
- Que se pueda registrar una partida.
- Que se pueda ingresar un concepto.
- Que se pueda ingresar un monto válido.
- Que se pueda registrar una fecha.
- Que el gasto aparezca en la tabla.
- Que el gasto quede asociado a la obra correspondiente.
- Que los datos permanezcan guardados después de reiniciar la aplicación.
- Que los cambios realizados estén registrados en GitHub.

## Evidencias

Las evidencias correspondientes al Sprint pueden incluir:

- Historial de commits en GitHub.
- Capturas del módulo de gastos.
- Capturas de gastos registrados.
- Datos almacenados en SQLite.
- Resultados de pruebas realizadas.

## Estado

Finalizado.