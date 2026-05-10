# Skills — Cómo escribir un SKILL.md de bicho

---

## Template

```markdown
---
description: [Qué hace y cuándo usarlo. Primera frase = el caso de uso principal.]
disable-model-invocation: true
allowed-tools: Bash Read
argument-hint: [argumentos opcionales]
---

# [Nombre] — [Subtítulo canónico]

[Identidad del bicho en 1-2 líneas. Tono Kvothesson: frío, técnico, con rastros de algo más.]

## Detección de plataforma

Antes de cualquier acción, detectar el OS:

```python
import platform
os_name = platform.system()  # 'Windows' | 'Darwin' | 'Linux'
```

## Si el usuario invoca `/bestiario:[nombre] [arg]`

[Instrucciones concretas, con ramas por OS donde corresponda.]

## Identidad canónica

[Frase canónica del bicho entre comillas itálicas.]
```

---

## Reglas de frontmatter

- `disable-model-invocation: true` siempre — los bichos se invocan a mano
- `allowed-tools` solo lo necesario — no dar permisos de más
- `description` empieza por el caso de uso, no por la identidad narrativa
- Usar `${CLAUDE_SKILL_DIR}` para referencias a archivos dentro del skill
- `WebSearch` y `WebFetch` solo si el bicho necesita internet (ej: Mainumby)

---

## Reglas de contenido

- Siempre detectar plataforma antes de actuar — ver `.agents/identidad.md` para el patrón
- Ramas explícitas por OS donde el comportamiento difiere
- Si una función no existe en un OS: decirlo en una línea, no fallar silenciosamente
- Identidad canónica al final, entre comillas itálicas