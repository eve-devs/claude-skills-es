---
name: explora-repo
description: >
  Levanta el mapa de un repositorio desconocido: arquitectura real, por donde entra
  una peticion, donde vive la logica de negocio, como se corre y como se testea.
  Pensado para el primer dia en un proyecto nuevo o para entender un repo de terceros.
  Usar cuando el usuario diga: "explicame este repo", "explora el proyecto", "no entiendo
  este codigo", "de que va este proyecto", "por donde empiezo", "onboarding", "primer dia",
  "como funciona este repo", "hazme un mapa del codigo", "donde esta la logica de".
---

# Explora repo

Produce un mapa util de un codebase desconocido en una pasada. El objetivo no es listar carpetas: es que alguien pueda **hacer su primer cambio** despues de leerlo.

## Regla base

Prioriza lo que el codigo hace sobre lo que el README dice que hace. Los READMEs mienten por omision; el codigo no.

## Paso 1 — Orientarse (barato, primero)

```bash
ls -la
cat README* 2>/dev/null | head -60
git log --oneline -15
git log --format='%an' | sort | uniq -c | sort -rn | head -5   # quien mantiene esto
```

Identifica el stack por los archivos de manifiesto:

| Archivo | Stack |
|---|---|
| `package.json` | Node / JS / TS — mira `scripts` y `dependencies` |
| `pyproject.toml`, `requirements.txt` | Python |
| `go.mod` | Go |
| `Cargo.toml` | Rust |
| `composer.json` | PHP |
| `pom.xml`, `build.gradle` | Java / Kotlin |
| `Gemfile` | Ruby |
| `docker-compose.yml` | Servicios externos (DB, cache, colas) |

`docker-compose.yml` y `.env.example` son oro: te dicen de que depende el proyecto para arrancar.

## Paso 2 — Encontrar el punto de entrada

No adivines. Buscalo:

- **Node**: campo `main`/`scripts.start` en `package.json`, luego `src/index.*`, `src/main.*`, `app.*`
- **Next.js / frameworks de archivos**: la estructura de `app/` o `pages/` **es** el enrutador
- **Python**: `if __name__ == "__main__"`, `main.py`, `wsgi.py`, `asgi.py`, `manage.py`
- **Go**: `func main()` en `cmd/`
- **Rust**: `src/main.rs`

```bash
grep -rn "if __name__" --include="*.py" . | head
grep -rln "func main()" --include="*.go" . | head
```

## Paso 3 — Seguir un flujo completo de punta a punta

Esto es lo que separa un mapa util de un indice inutil. Elige **una** operacion representativa (un login, un listado, el endpoint mas obvio) y siguela:

```
peticion HTTP -> ruta -> middleware -> controlador -> servicio -> acceso a datos -> respuesta
```

Anota los nombres de archivo y linea reales de cada salto. Ese recorrido le ensena al lector el patron que sigue todo lo demas.

## Paso 4 — Ubicar las piezas clave

- **Modelo de datos**: schemas, entidades, migraciones (`migrations/`, `prisma/schema.prisma`, `models/`)
- **Configuracion**: como se leen las variables de entorno y cuales son obligatorias
- **Autenticacion**: donde se valida la sesion o el token
- **Tests**: donde viven, como se corren, y que tanto cubren de verdad
- **Frontera con el exterior**: llamadas a APIs de terceros, colas, webhooks

## Paso 5 — Entregar el mapa

Formato de salida:

```markdown
# <nombre del repo>

**Que es:** una frase. Que problema resuelve y para quien.
**Stack:** lenguaje, framework, base de datos, infra.
**Estado:** ultimo commit, frecuencia, cuanta gente lo toca.

## Como correrlo
Los comandos exactos, en orden, incluyendo dependencias externas.

## Arquitectura
Las 4-6 piezas reales y como se hablan entre si.

## Recorrido de ejemplo: <operacion>
Ruta completa con archivo:linea en cada salto.

## Donde tocar para...
| Quiero... | Voy a... |
|---|---|
| agregar un endpoint | `src/routes/`, luego `src/services/` |
| cambiar el modelo | migracion en `...`, entidad en `...` |

## Lo que me llamo la atencion
Deuda tecnica visible, patrones raros, cosas que parecen trampa.
```

## Cuando el repo es grande

No leas todo. Muestrea:
- Los 10 archivos mas grandes (`find . -name "*.ts" -exec wc -l {} + | sort -rn | head`)
- Los 10 archivos mas modificados (`git log --format= --name-only | sort | uniq -c | sort -rn | head`) — ahi esta el corazon del proyecto

## Errores comunes

- Pegar el arbol de directorios completo y llamarle mapa.
- Describir carpetas (`utils/ tiene utilidades`) en vez de flujos.
- Confiar en los comandos del README sin verificar que los scripts existan en `package.json`.
- Omitir las dependencias externas necesarias para arrancar (la DB, el Redis, el `.env`).
