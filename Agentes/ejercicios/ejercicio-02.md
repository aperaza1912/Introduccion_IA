# Ejercicio 2 — Descripción PEAS de agentes inteligentes

## Contexto

En el capítulo 2 de *Artificial Intelligence: A Modern Approach* (Russell & Norvig),
un agente se entiende mejor cuando se especifica su **entorno de tarea**. Una forma
estándar de hacerlo es la descripción **PEAS**:

| Letra | Significado | Pregunta guía |
|---|---|---|
| **P** | *Performance* (medida de desempeño) | ¿Cómo se evalúa el éxito del agente? |
| **E** | *Environment* (entorno) | ¿En qué mundo opera? ¿Quién más actúa ahí? |
| **A** | *Actuators* (actuadores) | ¿Qué acciones puede ejecutar? |
| **S** | *Sensors* (sensores) | ¿Qué información puede percibir? |

Este ejercicio **no requiere programar**. Consiste en analizar distintos tipos de
aplicaciones reales y describir cada una con el esquema PEAS.

## Objetivo

Para cada una de las **8 aplicaciones** listadas abajo, redacta una descripción
PEAS completa y coherente. Debes pensar como diseñador del agente: qué optimiza,
dónde actúa, con qué puede mover o modificar el mundo, y qué puede observar.

## Aplicaciones a analizar

Describe PEAS para cada una de estas aplicaciones:

1. **Asistente virtual de voz** (p. ej. Siri, Alexa o Google Assistant en un altavoz inteligente).
   - Performance: Tiempo de respuesta entre usuario y agente; tasa de similitud entre el enunciado emitido por el usuario y el texto generado por el agente (tasa de reconocimiento de voz).
   - Environment: Físico - interior de una habitación u hogar, habitado por personas y con cantidad definida de dispositivos inteligentes. Parcialmente observable - la voz puede tener ruido de fondo. Estrocástico - factores como el clima pueden afectar la respuesta del modelo. Dinámico - los factores como temperatura y tiempo varían mientras el asistente ejecuta una tarea.
   - ~~Actuators: Altavoces y pantalla.~~
   - ~~Sensors: Botones de volumen, encendido y apagado de micrófono. Botón de acción. Micrófono.~~
2. **Robot aspirador doméstico** (p. ej. Roomba u otro robot que limpia pisos de un departamento).
   - Performance: Tasa de limpieza basado en el espacio que puede ser limpiado (ej: 30% de loa habitación, basado en el área transitable): Tiempo de ejecución de limpieza en un espacio de tamaño dado; Eficiencia energética - batería consumida por sesión o por metro cuadrado.
   - Environment:
   - Actuators: Mecanismo de aspirado. Dirección de las ruedas. Luces y bocinas que indican el estado de su tarea (batería baja, topar con una pared).
   - Sensors: Sensores de distancia y mapeo de la habitación. Sensores de suciedad. Sensor de carga.
3. **Sistema de recomendación de streaming** (p. ej. Netflix o Spotify que sugiere películas o canciones).
   - Performance: Score dado por el usuario (opiniones de la recomendación en sí); tasa de permanencia/retención en un contenido dada una recomendación; Número unidades de contenido consumidas a partir de una recomendación.
   - Environment:
   - Actuators: Generador de listas personalizadas; control de contenido siguiente dentro de dichas listas. Envío de notificaciones basadas en el gusto del usuario.
   - Sensors: Los sensores serían "digitales" - captación de calificaciones o likes del usuario, saltos en el contenido multimedia, registros de búsqueda. Si hablamos de un modelo avanzado, se puede recabar info de género, edad, e inclinaciones políticas/religiosas.
4. **Vehículo autónomo en ciudad** (conducción sin conductor en calles urbanas con tráfico y peatones).
   - Performance: Distancia recorrida basada en distancia máxima del trayecto (optimización del uso de combustible); tiempos de llegada previstos y reales; seguridad: porcentaje de éxito en situaciones de peligro o que puedan causar un comportamiento ilegal.
   - Environment:
   - Actuators: Generador de rutas. Giro y dirección (adelante, reversa, izquierda, derecha). Señalizadores viales, como luces frontales, traseras, preventivas y direccionales.
   - Sensors: Cámaras frontales, traseras y laterales. Sensores de detección de objetos alrededor del vehículo. Sensores de velocidad. GPS. Sensores de nivel de batería o gasolina.
5. **Agente de trading algorítmico en bolsa** (compra y venta automática de acciones en mercados financieros).
   - Performance: Proporción de ganancia después de venta de una acción; precisión del modelo de predicción de subida/baja de precios por acción;&#x20;
   - Environment:
   - Actuators: Sistema de venta o compra de acciones. Cancelador de compra/venta de las acciones.
   - Sensors: Datos históricos de las acciones o de las empresas dueñas de las acciones. Portales de noticias o sitios especializados en el análisis de la bolsa de valores. Datos de portafolios de otras personas o empresas que usan la bolsa de valores. Historial de precios.
6. **Sistema de diagnóstico médico asistido por IA** (apoya a un médico a interpretar síntomas e imágenes clínicas).
   - Performance: (dado por el médico) número de aciertos en la detección de características patológicas; tasa de éxito de detección de enfermedades. Sensibilidad del modelo; manejo de falsos y verdaderos positivos.
   - Environment:
   - Actuators:  Visualizador de imágenes en tiempo real con mapas de calor o profundidad. Generador de diagnóstico preliminar con la información disponible hasta el momento, con probabilidades de certeza. Sistema de detección de anomalías. Puede preguntar por más síntomas para hacer más preciso el resultado.
   - Sensors: Cámara. Sensores de proximidad. Interfaz UX para meter información manualmente.
7. **Dron de inspección de infraestructura** (revisa grietas, corrosión o fugas en puentes, tuberías o líneas eléctricas).
   - Performance: Porcentaje de infraestructura analizada; sensibilidad de falsos/verdaderos positivos en la detección de anomalías; número de choques/obstáculos evitados con éxito; autonomía de la batería.
   - Environment:
   - Actuators: Regular velocidad de las hélices. Encender o apagar transmisión de imágenes a dispositivos remotos.&#x20;
   - Sensors: Cámaras, sensores infrarojos y de proximidad. Sensor de movimiento y giroscopio. Sensores de estado de batería y temperatura del dispositivo. Receptor de señales de control remoto.
8. **Agente jugador de ajedrez** (programa que compite contra un humano u otro agente en partidas completas).
   - Performance: Porcentaje de partidas ganadas; promedio de número de movimientos necesarios para ganar la partida; suma de valor final de las piezas restantes al final del juego; número de veces que el agente pudo poner o estuvo en jaque.
   - Environment:
   - Actuators: Mover las piezas en distintas posiciones respetando distancias y reglas de juego.  Atrapar piezas dentro de las reglas permitidas. Avisar el movimiento de jaque o anticipar jugadas futuras del oponente. Cambiar las piezas cuando es necesario.
   - Sensors: Percepción del tablero después de una jugada. Memoria del historial de movimientos. Reloj de partida.

## Instrucciones

Para **cada** aplicación entrega una sección con este formato:

```markdown
### N. Nombre de la aplicación

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...
```

### Criterios de calidad

- **Performance:** incluye métricas concretas (precisión, tiempo, costo, satisfacción del usuario, ganancia, seguridad, etc.), no solo “hacerlo bien”.
- **Environment:** menciona si es parcialmente observable o totalmente observable, si es estocástico o determinista, episódico o secuencial, estático o dinámico, y discreto o continuo (según aplique).
- **Actuators:** lista acciones reales que el agente puede ejecutar, no capacidades vagas.
- **Sensors:** lista percepciones concretas (cámara, micrófono, API, historial de usuario, cotizaciones de mercado, etc.).

### Ejemplo breve (solo como referencia de formato)

**Aplicación:** termostato inteligente de una casa.

- **Performance:** mantener la temperatura deseada con mínimo consumo de energía y máxima comodidad del habitante.
- **Environment:** interior de una vivienda; cambia con clima exterior, ventanas abiertas y presencia de personas.
- **Actuators:** encender/apagar calefacción o aire acondicionado; ajustar temperatura objetivo; enviar alertas al usuario.
- **Sensors:** termómetro interior, horario, presencia (movimiento), lectura de clima exterior vía internet.

> El termostato **no** está en la lista de las 8 aplicaciones: es solo un ejemplo.
> Debes completar las ocho aplicaciones indicadas arriba.

## Entrega

Un documento (Markdown o PDF) con las **8 descripciones PEAS**, numeradas y con título
claro para cada aplicación.

Opcional pero recomendado: al final de cada descripción, añade **2–3 líneas** que
justifiquen por qué clasificaste el entorno como observable/estocástico/secuencial/etc.

## Criterios de aceptación

- No usar IA para generar las respuestas de este ejercicio.
- Hay exactamente **8** descripciones PEAS, una por cada aplicación de la lista.
- Cada descripción tiene los cuatro componentes (**P**, **E**, **A**, **S**) claramente identificados.
- Las respuestas son específicas de la aplicación (evita copiar la misma descripción genérica para todas).
- El entorno (**E**) incluye al menos una clasificación AIMA (p. ej. parcialmente observable, estocástico, secuencial).
- Redacción clara, en español, sin ambigüedades evidentes.

## Pistas

- Un mismo tipo de agente puede tener **distintos PEAS** según el contexto: un dron de inspección en un túnel no es igual que uno en un campo abierto.
- **Performance** y **Environment** suelen confundirse: la medida de desempeño dice *qué optimizas*; el entorno dice *dónde ocurre la tarea y qué condiciones enfrentas*.
- Si dudas entre dos sensores o actuadores, pregúntate: *¿esto lo usa el agente para decidir, o solo el humano que lo supervisa?* Solo cuenta lo que el **agente** percibe o controla.
