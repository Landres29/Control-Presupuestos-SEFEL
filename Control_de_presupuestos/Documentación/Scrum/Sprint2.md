# Sprint 2 - Registro de presupuestos y partidas

## Objetivo

Implementar el módulo de presupuestos del sistema, permitiendo registrar presupuestos asociados a una obra y organizar la información mediante partidas.

## Actividades

Durante este Sprint se consideran las siguientes actividades:

- Implementar el registro de presupuestos.
- Asociar cada presupuesto a una obra existente.
- Implementar el registro de partidas.
- Registrar montos presupuestados.
- Mostrar los presupuestos registrados en una tabla.
- Permitir consultar los presupuestos asociados a las obras.
- Guardar la información utilizando la base de datos SQLite.
- Verificar que los presupuestos permanezcan almacenados después de cerrar y volver a abrir la aplicación.

## Responsable

Desarrollador.

## Duración estimada

1 semana.

## Entregable

Módulo de presupuestos.

## Funcionalidades implementadas

### Registro de presupuestos

El sistema permite registrar un presupuesto asociado a una obra previamente creada.

Para registrar un presupuesto se consideran los siguientes datos:

- Obra.
- Partida.
- Monto presupuestado.

### Asociación con obras

Cada presupuesto se encuentra relacionado con una obra existente mediante la base de datos.

Esto permite identificar a qué obra corresponde cada presupuesto registrado.

### Registro de partidas

Las partidas permiten organizar los montos presupuestados de una obra.

Cada registro debe indicar el nombre o descripción de la partida y el monto correspondiente.

### Consulta de presupuestos

Los presupuestos registrados se muestran en una tabla para facilitar su consulta.

La tabla permite visualizar:

- Obra.
- Partida.
- Monto presupuestado.

### Persistencia de datos

Los presupuestos se almacenan en SQLite.

La información debe permanecer disponible después de cerrar y volver a ejecutar la aplicación.

## Validaciones iniciales

Durante el registro de presupuestos se consideran las siguientes validaciones básicas:

- Se debe seleccionar una obra.
- La partida no puede estar vacía.
- El monto presupuestado no puede estar vacío.
- El monto debe contener un valor numérico.
- El monto debe ser mayor que cero.

Las reglas específicas de caracteres válidos e inválidos serán definidas posteriormente en los requerimientos y casos de prueba.

## Control de versiones

Los cambios desarrollados durante este Sprint se registran mediante Git y GitHub.

Los commits correspondientes permiten identificar la incorporación progresiva del módulo de presupuestos y su conexión con la base de datos.

## Revisión del Sprint

Al finalizar el Sprint se debe comprobar:

- Que las obras existentes aparezcan en el selector de presupuestos.
- Que se pueda registrar una partida.
- Que se pueda ingresar un monto presupuestado válido.
- Que los datos registrados aparezcan en la tabla.
- Que un presupuesto quede asociado a la obra seleccionada.
- Que los datos permanezcan guardados después de reiniciar la aplicación.
- Que los cambios realizados estén registrados en GitHub.

## Evidencias

Las evidencias correspondientes al Sprint pueden incluir:

- Historial de commits en GitHub.
- Capturas del módulo de presupuestos.
- Capturas de presupuestos registrados.
- Datos almacenados en SQLite.
- Resultados de pruebas realizadas.

## Estado

Finalizado.