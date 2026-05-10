# Bestiario — Contexto de desarrollo

Plugin de Claude Code del universo Kvothesson. Cada bicho es un skill con identidad propia.

GitHub: https://github.com/kvothesson/bestiario-plugin

---

## Índice — leer según tarea

| Tarea | Archivo |
|---|---|
| Ver qué hace cada bicho, sus args y contexto técnico | [.agents/bichos.md](.agents/bichos.md) |
| Escribir o corregir un `SKILL.md` | [.agents/skills.md](.agents/skills.md) |
| Agregar bicho nuevo, checklist completo | [.agents/workflows.md](.agents/workflows.md) |
| Naming, tono, universo Kvothesson, reglas cross-platform | [.agents/identidad.md](.agents/identidad.md) |

---

## Estructura del repo

```
bestiario-plugin/
├── .agents/
│   ├── bichos.md        ← catálogo y contexto de cada bicho
│   ├── skills.md        ← cómo escribir un SKILL.md de bicho
│   ├── workflows.md     ← flujo completo para agregar bicho nuevo
│   └── identidad.md     ← naming, tono, universo Kvothesson, cross-platform
├── .claude-plugin/
│   └── plugin.json      ← metadata + version (bumpar al hacer release)
├── assets/              ← imágenes para el README
├── skills/
│   └── [nombre-bicho]/
│       ├── SKILL.md
│       └── [scripts de soporte]
├── README.md
└── AGENT.md             ← este archivo
```

---

## Reglas antes de commitear

Verificar que ningún archivo contiene rutas absolutas con nombre de usuario, paths a `.env`, tokens o credenciales, nombres de máquinas u organizaciones internas.

```bash
git diff --cached | grep -iE "Users/|Users\\|/home/[a-z]|\.env|api.key"
```

Si una ruta no funcionaría en la máquina de otra persona, no va al repo.