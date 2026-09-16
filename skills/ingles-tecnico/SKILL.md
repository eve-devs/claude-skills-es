---
name: ingles-tecnico
description: >
  Escribe o pule comunicacion tecnica en ingles de trabajo para devs hispanohablantes:
  mensajes de Slack, standups, comentarios de code review, descripciones de PR, correos
  al equipo, y respuestas dificiles (pedir mas tiempo, decir que no, reportar un bloqueo).
  Corrige los calcos del espanol y explica por que, para que la proxima salga sola.
  Usar cuando el usuario diga: "en ingles", "traduce esto", "como digo esto en ingles",
  "revisa mi ingles", "mensaje para mi equipo", "standup en ingles", "suena raro en ingles",
  "ingles tecnico", "escribe este correo en ingles", "como le digo a mi manager".
---

# Ingles tecnico

Para devs de LATAM trabajando con equipos en ingles. El objetivo no es ingles perfecto: es sonar como un colega competente y no perder autoridad tecnica por la traduccion.

## Regla base

No traduzcas palabra por palabra. Identifica que intenta lograr el mensaje y escribelo como lo escribiria un dev nativo en ese canal.

Entrega siempre **dos cosas**: el mensaje listo para copiar, y una nota corta de que cambio y por que. La nota es lo que hace que mejore con el tiempo.

## Calcos del espanol que delatan

| Se escribe | Suena | Se dice |
|---|---|---|
| "I have a doubt" | raro (duda = desconfianza) | "I have a question" / "Quick question:" |
| "Actually" por "actualmente" | "en realidad" | "Currently" |
| "I will inform you" | rigido, de oficio | "I'll let you know" |
| "Please, can you..." | la coma suena a suplica | "Could you..." |
| "I am agree" | agramatical | "I agree" |
| "Until Friday" por "hasta el viernes" | ambiguo | "by Friday" (fecha limite) |
| "Realize" por "realizar" | "darse cuenta" | "carry out" / "do" |
| "Assist to the meeting" | asistir ≠ assist | "attend the meeting" |
| "Support" por "soportar/aguantar" | ok en soporte tecnico | "handle" / "tolerate" |
| "Explain me" | agramatical | "Explain it to me" / "Walk me through" |
| "In the morning I..." + pasado | calco de orden | ordenar sujeto-verbo primero |
| "Sorry for the late response" en cada mensaje | inseguridad | omitir, o "Thanks for your patience" |

## Registro por canal

| Canal | Tono | Largo |
|---|---|---|
| Slack | directo, minusculas ok, sin saludo formal | 1-3 lineas |
| Standup | telegrafico, tres bloques | 3-5 lineas |
| Code review | suave en la forma, firme en el fondo | 1-2 lineas por comentario |
| Descripcion de PR | estructurado, impersonal | parrafos cortos |
| Correo | saludo + contexto + pedido claro | 4-8 lineas |

## Plantillas

**Standup:**
```
Yesterday: finished the token refresh fix, PR is up.
Today: starting on the rate limiter.
Blockers: waiting on staging credentials from infra.
```

**Code review — pedir un cambio sin sonar agresivo:**
```
Could we pull this into a helper? It's duplicated in `auth.ts` too.
```
```
Small thing: this will throw if `user` is null. Worth a guard?
```
El ingles de code review usa preguntas y diminutivos ("small thing", "nit:", "worth a...?") no por timidez, sino porque es la convencion. Un imperativo directo ("Change this") se lee mas duro de lo que suena en espanol.

**Reportar un bloqueo sin sonar a excusa:**
```
Heads up: I'm blocked on the staging credentials. I've moved to the
rate limiter meanwhile, but the auth PR won't land today unless I get
access. Who's the right person to ask?
```
Patron: hecho -> que hiciste igual -> impacto concreto -> pedido especifico.

**Pedir mas tiempo:**
```
This is taking longer than I estimated — the migration touches three
services instead of one. Realistic date is Thursday. Happy to cut scope
if Tuesday matters more.
```
Nunca pidas disculpas de entrada. Da el dato, la fecha nueva, y una opcion.

**Decir que no / empujar de vuelta:**
```
I'd push back on that a bit. Doing it that way means we'd need to
X, and we'd lose Y. What if we did Z instead?
```

## Frases que suben el registro sin sonar forzadas

- "Heads up:" — aviso corto
- "Quick question:" — abre sin disculparse
- "Worth a look?" — sugiere sin imponer
- "Makes sense to me." — aprueba sin efusividad
- "I'd lean toward X." — opina con propiedad
- "Let me dig into it and get back to you." — gana tiempo profesionalmente
- "Just to make sure I understood:" — confirma sin admitir confusion

## Cuando el usuario ya escribio algo

1. Devuelve la version corregida primero, lista para copiar.
2. Debajo, maximo 3 notas: que cambiaste y por que.
3. No corrijas cosas que ya estaban bien. Un mensaje que sirve no se reescribe por gusto.

Si el original ya esta bien, dilo y no toques nada.

## Errores comunes

- Subir el registro de mas: un mensaje de Slack que parece carta notarial.
- Traducir el humor o los modismos. Casi nunca cruzan; se quitan.
- Pedir disculpas en exceso — en ingles de trabajo lee como falta de confianza.
- Mandar un parrafo donde una linea alcanza.
