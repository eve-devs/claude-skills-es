# Contribuir

Gracias por querer aportar. Este repo acepta skills nuevas y mejoras a las existentes.

## Qué entra aquí

Skills que cumplan las tres:

1. **En español**, con triggers que la gente realmente teclea en español.
2. **Útiles para cualquiera**, no para un proyecto o empresa en particular.
3. **Con opiniones.** Una skill que solo dice "sé cuidadoso y sigue buenas prácticas" no aporta nada sobre el comportamiento por defecto de Claude. Las buenas toman decisiones: este formato, este orden, esto nunca.

## Qué no entra

- Skills con datos privados: tarifas, clientes, credenciales, información de tu empresa.
- Traducciones directas de skills que ya existen en inglés.
- Skills que solo envuelven un comando (`git status` no necesita una skill).

## Cómo agregar una skill

1. Crea `skills/<nombre>/SKILL.md`. El nombre va en kebab-case y en español.
2. El encabezado necesita `name` y `description`. La descripción tiene que terminar con las frases de activación:
   `Usar cuando el usuario diga: "...", "...", "..."`.
3. Escribe el cuerpo en secciones cortas. Si algo se decide con una tabla, usa una tabla.
4. Cierra con una sección de **Errores comunes**. Es la parte que más cambia el resultado.
5. Agrega tu skill a la tabla del README.

## Probarla antes del PR

```bash
cp -r skills/<nombre> ~/.claude/skills/
```

Abre una sesión nueva de Claude Code y pídele algo con tus frases de activación. Si la skill no se enciende, el problema está en la descripción, no en el cuerpo.

Prueba también que **no** se encienda cuando no toca. Una skill que se activa de más es peor que una que se activa de menos.

## Estilo

- Tuteo, directo, sin relleno corporativo.
- Sin emojis dentro de los `SKILL.md`.
- Ejemplos reales de código antes que explicaciones abstractas.
- Cuando des una regla, di por qué. Claude sigue mejor las reglas que entiende.

## Regenerar el GIF de demo

```bash
python3 -m venv venv && ./venv/bin/pip install Pillow
./venv/bin/python dev/make-demo.py
```
