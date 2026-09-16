---
name: pr-listo
description: >
  Prepara un pull request completo a partir del diff real de la rama: titulo, descripcion
  con contexto y decisiones, plan de pruebas, y una auto-revision que detecta lo que falta
  (tests, migraciones, docs, cambios rompientes) antes de que lo vea un reviewer.
  Usar cuando el usuario diga: "prepara el PR", "abre un pull request", "descripcion del PR",
  "que le pongo al PR", "revisa mi rama antes de subirla", "esta listo para review",
  "PR listo", "sube esto a review", "checklist antes del PR".
---

# PR listo

Un PR bien armado se aprueba mas rapido porque le ahorra trabajo al reviewer. Esta skill produce ese PR y, antes, encuentra lo que el reviewer iba a encontrar.

## Paso 1: leer la rama completa

```bash
BASE=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@.*/@@' || echo main)
git log --oneline "origin/$BASE"..HEAD
git diff "origin/$BASE"...HEAD --stat
git diff "origin/$BASE"...HEAD
```

Tres puntos (`...`), no dos: compara contra el ancestro comun, que es lo que el reviewer vera en GitHub.

## Paso 2: auto-revision

Antes de escribir la descripcion, busca lo que falta. Reporta cada hallazgo con archivo y linea:

**Lo que bloquea:**
- Secretos o credenciales en el diff
- Restos de debug: `console.log`, `print()`, `debugger`, `.only`, `.skip`
- Codigo comentado sin explicacion
- Cambios rompientes de API sin nota (firma de funcion, campo de respuesta eliminado, endpoint renombrado)
- Migracion de base de datos sin su reversa (`down`)

**Lo que hay que preguntar:**
- Logica nueva sin ningun test que la toque
- Variable de entorno nueva que no esta en `.env.example`
- Dependencia nueva: ¿hace falta o el repo ya tiene algo equivalente?
- Comportamiento documentado en el README que este PR cambia
- Archivos de mas de ~400 lineas de diff que probablemente deban dividirse

## Paso 3: escribir el PR

**Titulo:** mismo formato que los commits del repo (`git log --oneline -20` para confirmar). Describe el resultado, no el proceso.

```
mal:  Cambios del ticket 482
bien: fix(auth): evitar refresh infinito al expirar el token
```

**Descripcion:**

```markdown
## Que cambia
Dos o tres frases. Que hace distinto el sistema despues de este PR.

## Por que
El problema o el requerimiento. Enlaza el issue si existe.

## Como
Solo si la solucion no es obvia leyendo el diff. Aqui van las decisiones:
que alternativa descartaste y por que.

## Como probarlo
Pasos numerados y reproducibles.
1. `npm run dev`
2. Entrar a `/login` con un token expirado
3. Esperado: una sola peticion de refresh, luego 401 limpio

## Notas para quien revisa
- El archivo X tiene 300 lineas de diff pero es solo el formateo automatico
- La migracion hay que correrla antes de desplegar
```

Escribe la descripcion en el idioma del repo. Si los PRs anteriores estan en ingles, este tambien.

## Paso 4: crear el PR

Confirma con el usuario antes de publicar nada. Publicar un PR es una accion hacia afuera: el equipo recibe notificaciones.

```bash
git push -u origin "$(git branch --show-current)"
gh pr create --title "..." --body-file /tmp/pr-body.md --base "$BASE" --draft
```

Usa `--draft` si la auto-revision encontro cosas sin resolver. Si el repo tiene `.github/pull_request_template.md`, rellena **esa** plantilla en vez de la de arriba.

## Errores comunes

- Describir los commits uno por uno. Al reviewer le importa el resultado final.
- "Como probarlo: correr los tests". Eso ya lo hace CI; di que probar a mano.
- Un PR que mezcla refactor y feature: se revisa mal y se revierte peor. Ofrece dividirlo.
- Abrir el PR contra la rama equivocada.
