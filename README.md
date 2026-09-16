# Claude Skills en español

Skills para [Claude Code](https://claude.com/claude-code) escritas en español, para devs de LATAM.

La mayoría de las skills que existen están en inglés — y como Claude decide qué skill activar leyendo su descripción, una skill con triggers en inglés simplemente no se enciende cuando escribes "prepara el PR" o "explícame este repo". Estas sí.

## Instalación

```bash
/plugin marketplace add eve-devs/claude-skills-es
/plugin install claude-skills-es
```

Eso es todo. Las skills se activan solas cuando lo que pides coincide con lo que hacen.

## Qué incluye

| Skill | Qué hace | Se activa con |
|---|---|---|
| **commit-limpio** | Lee el diff real y arma commits atómicos con mensajes que se entienden en seis meses. Detecta secretos y restos de debug antes de commitear. | "haz commit", "commits atómicos", "qué mensaje le pongo" |
| **explora-repo** | Mapa de un repo desconocido: arquitectura real, por dónde entra una petición, dónde tocar para cada cosa. Para tu primer día. | "explícame este repo", "por dónde empiezo", "no entiendo este código" |
| **readme-pro** | Escribe o arregla un README partiendo del código, verificando que cada comando que documenta exista de verdad. | "hazme un README", "documenta este proyecto" |
| **pr-listo** | Prepara el PR completo y hace la auto-revisión antes: qué tests faltan, qué migración no tiene reversa, qué rompe. | "prepara el PR", "¿está listo para review?" |
| **ingles-tecnico** | Standups, code reviews, Slack y correos difíciles en inglés de trabajo. Corrige los calcos del español y te explica por qué. | "cómo digo esto en inglés", "revisa mi inglés" |

## Cómo se ve

```
> prepara el PR de esta rama

Revisé los 8 commits contra origin/main. Antes de la descripción,
tres cosas que el reviewer iba a encontrar:

  ⚠  src/auth/interceptor.ts:44 — console.log con el token completo
  ⚠  migrations/0012_add_sessions.sql — no tiene down
  ?  services/rate-limiter.ts — lógica nueva sin ningún test

¿Los arreglo antes de abrir el PR, o lo subo como draft?
```

## Usar una skill sin instalar el plugin

Cada skill es una carpeta con un `SKILL.md`. Copia la que quieras a tu carpeta de skills:

```bash
git clone https://github.com/eve-devs/claude-skills-es
cp -r claude-skills-es/skills/commit-limpio ~/.claude/skills/
```

`~/.claude/skills/` la deja disponible en todos tus proyectos. `.claude/skills/` dentro de un repo la limita a ese proyecto.

## Escribir tu propia skill

Una skill son dos cosas: un encabezado y unas instrucciones.

```markdown
---
name: mi-skill
description: >
  Qué hace, en una o dos frases. Y luego las frases exactas con las que
  el usuario la va a pedir — esto es lo que decide si se activa o no.
---

# Mi skill

Las instrucciones que quieres que Claude siga cuando esto se active.
```

Claude lee **solo la descripción** de todas tus skills al arrancar; carga el resto del archivo únicamente cuando tu petición coincide. Por eso la descripción vale más que el cuerpo: una skill excelente con una descripción vaga nunca se enciende.

Tres cosas que aprendí escribiendo estas:

- **Pon los triggers literales.** No "ayuda con git" sino las frases que la gente teclea: "haz commit", "qué mensaje le pongo".
- **Escribe reglas, no descripciones.** "Nunca escribas un mensaje sin leer el diff" funciona; "es importante leer el diff" no.
- **Incluye los errores comunes.** Decirle a Claude qué *no* hacer corrige más que decirle qué sí.

## Contribuir

Los PRs son bienvenidos — sobre todo skills nuevas en español. Lee [CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

MIT — [Evelyn Arias](https://github.com/eve-devs)
