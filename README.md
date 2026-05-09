# Retos de Analisis de Algoritmos

Repositorio academico con soluciones a retos de programacion desarrollados para la asignatura **Analisis de Algoritmos**. Los ejercicios estan basados principalmente en problemas de LeetCode y se presentan con su respectivo codigo fuente en Python, analisis de complejidad y evidencias visuales de resolucion.

## Objetivo

El objetivo de este repositorio es documentar las actividades practicas realizadas durante el curso, aplicando diferentes estrategias de diseno y analisis de algoritmos, tales como fuerza bruta, estructuras hash, algoritmos voraces y programacion dinamica.

## Contenido Del Repositorio

| Carpeta | Problema | Plataforma | Tecnica principal | Evidencia |
|---|---|---|---|---|
| `Clase 14 feb reto` | Two Sum | LeetCode | Fuerza bruta y Hash Map | Capturas de solucion |
| `Clase 21 feb reto` | Maximum Subarray | LeetCode | Fuerza bruta y Kadane | Capturas de solucion |
| `Clase 28 feb reto` | Non-overlapping Intervals | LeetCode | Greedy | Captura de estrategia |
| `Clase 7 marzo` | Climbing Stairs | LeetCode | Programacion dinamica | Captura de solucion |
| `Clase 7 marzo` | Maximum Subarray | LeetCode | Programacion dinamica / Kadane | Captura de solucion |
| `Clase 14 marzo reto` | House Robber | LeetCode | Programacion dinamica | Capturas de problema y envio |
| `Clase 14 marzo reto` | Min Cost Climbing Stairs | LeetCode | Programacion dinamica | Capturas de problema y envio |

## Retos Implementados

### Two Sum

Archivo: `Clase 14 feb reto/Ejercicio_1_two_sum.py`

Se implementan dos soluciones:

| Enfoque | Descripcion | Tiempo | Espacio |
|---|---|---|---|
| Fuerza bruta | Revisa todas las parejas posibles de indices. | `O(n^2)` | `O(1)` |
| Hash Map | Guarda valores visitados para encontrar el complemento en una sola pasada. | `O(n)` | `O(n)` |

### Maximum Subarray

Archivos:

- `Clase 21 feb reto/Ejercicio_53_Maximum_Subarray.py`
- `Clase 7 marzo/maximum_subarray.py`

Se resuelve el problema de encontrar el subarreglo contiguo con suma maxima. Se incluye una solucion por fuerza bruta y una solucion optimizada usando el algoritmo de Kadane.

| Enfoque | Tiempo | Espacio |
|---|---|---|
| Fuerza bruta | `O(n^2)` | `O(1)` |
| Kadane / DP optimizada | `O(n)` | `O(1)` |

### Non-overlapping Intervals

Archivo: `Clase 28 feb reto/Ejercicio_435 - Intervalos no superpuestos.py`

El problema se resuelve con una estrategia greedy: ordenar los intervalos por su punto de finalizacion y conservar la mayor cantidad posible de intervalos no solapados. La respuesta corresponde a los intervalos que deben eliminarse.

| Enfoque | Tiempo | Espacio |
|---|---|---|
| Greedy por tiempo de finalizacion | `O(n log n)` | `O(1)` adicional |

### Climbing Stairs

Archivo: `Clase 7 marzo/climb_stairs.py`

Se aplica programacion dinamica para contar las formas de llegar al escalon `n`, usando la recurrencia:

```text
dp[i] = dp[i - 1] + dp[i - 2]
```

La implementacion optimiza el espacio utilizando solo los dos estados anteriores.

| Tiempo | Espacio |
|---|---|
| `O(n)` | `O(1)` |

### House Robber

Archivo: `Clase 14 marzo reto/house_robber.py`

Se resuelve con programacion dinamica, evaluando en cada casa si conviene robarla o no. La recurrencia utilizada es:

```text
dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
```

| Tiempo | Espacio |
|---|---|
| `O(n)` | `O(1)` |

### Min Cost Climbing Stairs

Archivo: `Clase 14 marzo reto/min_cost_climbing_stairs.py`

Se calcula el costo minimo para llegar al tope de la escalera mediante programacion dinamica. La recurrencia usada es:

```text
dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
```

| Tiempo | Espacio |
|---|---|
| `O(n)` | `O(1)` |

## Tecnologias Utilizadas

- Python 3
- LeetCode
- Git y GitHub para control de versiones
- Capturas de pantalla como evidencia de resolucion

## Estructura General

```text
.
|-- Clase 14 feb reto/
|-- Clase 21 feb reto/
|-- Clase 28 feb reto/
|-- Clase 7 marzo/
|-- Clase 14 marzo reto/
`-- README.md
```

Cada carpeta contiene el codigo fuente correspondiente al reto trabajado en clase o como tarea, junto con capturas de pantalla que evidencian la resolucion del problema.

## Conceptos Aplicados

- Analisis de complejidad temporal y espacial.
- Comparacion entre soluciones por fuerza bruta y soluciones optimizadas.
- Uso de diccionarios para busqueda eficiente.
- Algoritmos voraces para problemas de seleccion optima.
- Programacion dinamica con optimizacion de espacio.
- Algoritmo de Kadane para subarreglos de suma maxima.

## Nota Academica

Este repositorio fue elaborado con fines academicos para registrar las soluciones desarrolladas durante la asignatura **Analisis de Algoritmos**. Las capturas incluidas funcionan como evidencia de la resolucion o envio de los ejercicios en la plataforma correspondiente.
