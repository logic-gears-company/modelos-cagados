# GPT-2 Small Spanish — First Test

**Modelo:** `datificate/gpt2-small-spanish`  
**Tipo:** GPT-2 pequeño / generación autoregresiva  
**Objetivo:** comprobar generación básica de texto en español.

---

## Carga del modelo

```text
Cargando GPT-2 español...
Loading weights: 100%|██████████████████████████████████████████████| 149/149 [00:00<00:00, 19755.06it/s]

[transformers] GPT2LMHeadModel LOAD REPORT from: /root/Modelos/models/gpt2-small-spanish

Key                                     | Status     |  |
----------------------------------------+------------+--+-
transformer.h.{0...11}.attn.masked_bias | UNEXPECTED |  |

Notes:
- UNEXPECTED: can be ignored when loading from different task/architecture; not ok if you expect identical arch.

Modelo listo.
```

## Prueba 1 — `hola`

```text
hola de Cueca y por el mismo lugar donde está la población del pueblo, al noroeste de la ciudad. En el lado de la población, a mitad de camino se encuentra el puente de la Vía Cueca.

La ciudad de Caca se encuentra situada en el extremo norte de la provincia de Jaén (Andalucía) y a 3 kilómetros de la ciudad de Jaén, aproximadamente en el límite entre la provincia de Jaén y la de Jaén, en la zona central de España.

El municipio limita al norte con la localidad de Caca, al sur con Caca del Río
```

**Observación:** genera español reconocible, pero mezcla lugares y hechos aparentemente inventados.

---

## Prueba 2 — `Colombia es un pais`

```text
Colombia es un paisano de clase media, pero también un aficionado al deporte del golf y al golf. Su hermano, Tony, es también jugador y jugador aficionado de golf y también ha jugado a través de clubes y universidades.

El padre de Tony se mudó a Los Ángeles, California cuando Tony tenía siete años cuando su madre fue a vivir con su madre en un barrio de clase media en el estado de California, y se graduó de la escuela de secundaria.

Tras la muerte de su madre en 2003, Tony asistió a la Universidad de California en Los Ángeles en una licenciatura en ingeniería, donde se graduó con
```

**Observación:** continúa el texto como si fuera prosa enciclopédica, pero deriva hacia una historia aparentemente inventada.

---

## Prueba 3 — `La inteligencia artificial es`

```text
Tú: La inteligencia artificial es capaz de generar inteligencia artificial que puede ser utilizada para crear nuevas situaciones en el mundo real o para crear nuevos tipos de armas.

"Los juegos de rol" (también conocido como "juego de rol"), más conocido como "juego de acción" o simplemente "juego de rol", son un tipo de juegos que en su mayoría son simulados en tiempo real, es decir, que usan la mecánica del juego de rol como un medio para hacer un juego que sea más fácil y menos repetitivo.
```

---

## Prueba 4 — `En España, el fútbol es`

```text
En España, el fútbol es un deporte de exhibición, de exhibición y de exhibición.

La categoría más popular de fútbol del país es el fútbol femenino.

En la actualidad hay un equipo femenino de fútbol, que juega en la Liga Nacional Femenina de Fútbol desde la temporada 2012. En la liga nacional femenina existen dos equipos, el Club Deportivo Alboia y el Club Deportivo Barcelona.
```

---

## Prueba 5 — `Mi nombre es Marcos y`

```text
Tú: Mi nombre es Marcos y me voy a casar con un hombre llamado Marcos. Mi nombre es Marcos y me voy a casar con mi hijo, el hijo de Marcos. Mi nombre es Marcos y me voy a casar con mi hija, la hija de Marcos. Mi nombre es Marcos y me voy a casar con el hijo del hijo de Marcos. Su nombre es Marcos y me voy a casar con mi hija.

El día 30 de enero de 2009, el Papa Francisco, con el apoyo de la Congregación para las Iglesias Orientales, declaró la ley de matrimonio entre los hermanos menores de edad de un niño, y ordenó al sacerdote
```

**Observación:** presenta repeticiones, relaciones familiares contradictorias y cambios abruptos de tema.

---

## Conclusión

El modelo funciona técnicamente: carga, genera texto y produce español reconocible. Sin embargo, no es un modelo conversacional y presenta repeticiones, incoherencias y contenido aparentemente inventado.

**Estado:** `WORKING / EXPERIMENTAL`

**Fecha de prueba:** 2026-09-24
