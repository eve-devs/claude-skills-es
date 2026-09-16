---
name: readme-pro
description: >
  Escribe o arregla el README de un proyecto partiendo del codigo real, no de una
  plantilla generica. Verifica que cada comando que documenta exista de verdad, ordena
  el contenido por lo que el lector necesita primero, y elimina el relleno de badges
  y emojis que no aportan. Usar cuando el usuario diga: "hazme un README", "mejora el
  readme", "documenta este proyecto", "el readme esta viejo", "readme profesional",
  "escribe la documentacion", "mi repo no tiene readme", "actualiza el readme".
---

# README pro

Un buen README responde tres preguntas en los primeros 30 segundos: **que es esto**, **me sirve a mi**, y **como lo corro**. Todo lo demas va despues.

## Regla base

Cada comando, ruta y variable que escribas tiene que existir en el repo. Si no lo verificaste, no lo pongas.

```bash
cat package.json | grep -A20 '"scripts"'   # los scripts que SI existen
cat .env.example 2>/dev/null               # las variables que SI se usan
ls docs/ 2>/dev/null
```

Un README con un `npm run dev` que no existe es peor que no tener README: quema la confianza del lector en la primera linea que intenta.

## Estructura

Este orden no es decorativo — sigue el momento de duda del lector.

```markdown
# Nombre del proyecto

Una o dos frases: que hace y para quien. Sin "una solucion moderna y robusta".

![demo o screenshot]        <- si es visual, va aqui. Vale mas que 3 parrafos.

## Instalacion

Requisitos previos concretos (version de Node, Python, Docker...).
Los comandos exactos, copiables, en orden.

## Uso

El caso de uso mas comun, con codigo real que se pueda pegar y correr.
Muestra la salida esperada.

## Configuracion

Tabla de variables de entorno: nombre, si es obligatoria, valor por defecto, para que sirve.

## Como funciona          <- opcional, solo si no es evidente

## Contribuir             <- solo si aceptas contribuciones de verdad

## Licencia
```

## Reglas de escritura

- **El titulo dice que es, no como se llama.** "Cliente de Postgres con reintentos" le sirve mas al lector que "Turbopg".
- **Muestra, no describas.** Un bloque de codigo con entrada y salida gana a un parrafo explicativo.
- **Sin superlativos.** "rapido", "moderno", "potente", "robusto" no significan nada. Si es rapido, pon el numero.
- **Badges: maximo 3**, y solo los que informan (build, version, licencia). Una fila de 12 badges es ruido.
- **Emojis: cero o casi.** Un README lleno de emojis se lee como generado por IA, que es justo lo que no quieres.
- **Tabla de contenidos** solo si el README pasa de ~150 lineas.

## Variables de entorno

Siempre en tabla, nunca en prosa:

| Variable | Obligatoria | Default | Descripcion |
|---|---|---|---|
| `DATABASE_URL` | si | — | Cadena de conexion a Postgres |
| `PORT` | no | `3000` | Puerto del servidor HTTP |

Saca los nombres del codigo real (`grep -rn "process.env\.\|os.environ\|getenv" src/`), no del `.env` local del usuario — y **nunca** copies valores reales.

## Arreglar un README existente

No lo reescribas entero de entrada. Diagnostica primero y reporta:

1. ¿Los comandos siguen existiendo? (contrasta contra `scripts` del manifiesto)
2. ¿Las rutas de archivo siguen existiendo?
3. ¿Falta alguna variable de entorno que el codigo si usa?
4. ¿Hay secciones que documentan features borradas?
5. ¿El orden entierra la instalacion debajo de tres parrafos de marketing?

Luego propon los cambios por seccion. Respeta el tono y el idioma que ya tiene el repo.

## Idioma

Si el proyecto apunta a un publico hispanohablante, README en espanol. Si es open source con intencion de alcance internacional, ingles — y opcionalmente un `README.es.md` enlazado desde arriba. Pregunta si no queda claro.

## Errores comunes

- Plantillas con secciones vacias ("## Roadmap — TBD").
- Documentar la instalacion desde el codigo fuente cuando el 95% de la gente solo quiere `npm install paquete`.
- Un ejemplo de uso que no compila.
- Mezclar README (para usuarios) con notas de arquitectura (para contribuidores). Eso va en `CONTRIBUTING.md` o `docs/`.
