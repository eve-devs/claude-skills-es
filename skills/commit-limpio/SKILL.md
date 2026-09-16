---
name: commit-limpio
description: >
  Convierte un working tree desordenado en commits atomicos con mensajes en formato
  Conventional Commits, leyendo el diff real en vez de inventar. Agrupa cambios que
  van juntos, separa los que no, y detecta secretos o archivos basura antes de commitear.
  Usar cuando el usuario diga: "haz commit", "commitea esto", "mensaje de commit",
  "separa los commits", "commits atomicos", "que mensaje le pongo", "conventional commits",
  "limpia mis cambios antes de subir", "prepara el commit".
---

# Commit limpio

Genera commits que un reviewer pueda leer en seis meses y entender **por que** se hizo el cambio, no solo que archivos se tocaron.

## Regla base

Nunca escribas un mensaje de commit sin haber leido el diff. Un mensaje inventado a partir de nombres de archivo es ruido.

## Paso 1: leer el estado real

```bash
git status --short
git diff --stat
git diff              # cambios sin stage
git diff --staged     # cambios ya en stage
```

Si el diff es enorme, lee primero `--stat` para ubicarte y luego el diff de los archivos que importan.

## Paso 2: revisar antes de commitear

Bloquea el commit y avisa al usuario si encuentras:

- **Secretos**: `.env`, tokens, claves API, cadenas tipo `sk-`, `ghp_`, `AKIA`, passwords en texto plano, archivos `.pem` o `.key`.
- **Basura**: `node_modules/`, `dist/`, `.DS_Store`, `*.log`, carpetas de build, archivos de mas de ~1 MB que no sean assets intencionales.
- **Restos de debug**: `console.log`, `print()`, `debugger`, `TODO: quitar esto`, tests con `.only` o `.skip`.

Estas cosas se reportan, no se borran por tu cuenta.

## Paso 3: agrupar en commits atomicos

Un commit = un cambio con sentido propio. Si el mensaje necesita un "y" para describirse, son dos commits.

| Situacion | Que hacer |
|---|---|
| Feature + refactor mezclados | Separar: primero el refactor, luego la feature encima |
| Fix + formateo automatico | Separar: el formateo esconde el fix en el diff |
| Varios archivos, un solo cambio logico | Un solo commit |
| Bump de dependencia + el codigo que lo usa | Juntos, si uno rompe sin el otro |

Para separar por partes de un mismo archivo usa `git add -p`, pero como `-i`/`-p` son interactivos y no funcionan en este entorno, aplica los hunks con `git apply --cached` a partir de un parche, o pide al usuario que corra `git add -p` el mismo.

## Paso 4: escribir el mensaje

Formato Conventional Commits:

```
<tipo>(<alcance>): <resumen en imperativo, minuscula, sin punto final>

<cuerpo: POR QUE, no que. Solo si el por que no es obvio.>

<footer: BREAKING CHANGE: ... / Closes #123>
```

Tipos: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `build`, `ci`, `chore`, `style`, `revert`.

El resumen va en **≤ 50 caracteres** y responde a "si aplico este commit, va a...".

**Espanol o ingles:** mira los ultimos 20 commits con `git log --oneline -20` y sigue el idioma y el estilo que ya usa el repo. No impongas Conventional Commits en un repo que claramente no lo usa; avisa y ofrece.

### Bien vs mal

```
mal:  cambios varios
mal:  fix: arregle el bug
mal:  feat: agregue el archivo UserService.ts al proyecto

bien: fix(auth): evitar refresh infinito al expirar el token

      El interceptor reintentaba la peticion original sin marcarla,
      asi que un 401 en el propio refresh disparaba otro refresh.
      Ahora se marca con _retry y se corta a la segunda.

      Closes #482
```

## Paso 5: confirmar antes de ejecutar

Muestra el plan (que archivos van en que commit, con que mensaje) y espera luz verde antes de correr `git commit`. Nunca hagas `push` salvo que te lo pidan explicitamente.

Si la rama actual es `main` o `master`, avisa y ofrece crear una rama primero.

## Errores comunes

- Correr `git add .` sin mirar que arrastras.
- Usar `feat` para un cambio que no agrega funcionalidad al usuario.
- Escribir el cuerpo describiendo el diff (el diff ya se ve solo) en vez del motivo.
- Amend sobre un commit ya pusheado sin avisar que reescribe historia.
