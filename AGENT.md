# Bestiario — Contexto de desarrollo

Plugin de Claude Code del universo Kvothesson. Cada bicho es un skill con identidad propia.

## Reglas antes de commitear

Antes de cualquier `git add` o `git commit`, verificar que ningún archivo contiene:

- Rutas absolutas con nombre de usuario (`C:\Users\[nombre]\`, `/home/[nombre]/`)
- Paths a archivos `.env`, claves, tokens o credenciales
- Referencias a directorios personales que no sean genéricos (`~`, `$env:USERPROFILE`, `$HOME`)
- Nombres de máquinas, organizaciones internas o datos de red

**Regla práctica:** si una ruta no funcionaría en la máquina de otra persona, no va al repo.

**Cómo reemplazar:**

| En vez de... | Usar... |
|---|---|
| `C:\Users\<nombre>\alguna\carpeta\` | `~/alguna/carpeta/` o `$env:USERPROFILE\alguna\carpeta\` |
| Path a un `.env` personal | `~/.env` o variable de entorno documentada |
| Path hardcodeado a script del plugin | `${CLAUDE_SKILL_DIR}/script.py` |

Si hay dudas, correr antes del commit:
```powershell
git diff --cached | Select-String "Users\\|/home/|\.env|api.key" -CaseSensitive
```

---

## Repo y estructura

```
C:\Users\ezequ\.claude\plugins\marketplaces\local\plugins\bestiario\
├── .claude-plugin\
│   └── plugin.json          ← metadata + version (bumpar al hacer release)
├── assets\                  ← imágenes para el README
│   ├── cover.png
│   └── mboi-portrait.png
├── skills\
│   └── [nombre-bicho]\
│       ├── SKILL.md         ← el bicho en sí
│       ├── analyze.py       ← scripts de soporte (si aplica)
│       └── tracker\         ← archivos que el bicho instala (si aplica)
├── README.md
└── AGENT.md                 ← este archivo
```

GitHub: https://github.com/kvothesson/bestiario-plugin

## Bichos existentes

| Bicho | Skill | Función |
|---|---|---|
| Mbói | `/bestiario:mboi` | Observador silencioso. Analiza `~/tracker/activity.db` y detecta fricciones. |

**Mbói — contexto adicional:**
- El tracker (`~/tracker/tracker.py`) corre en background y graba actividad de ventanas en SQLite
- `analyze.py` dentro del skill lee la DB y reporta patrones
- Shortcut en Windows Startup arranca el tracker al inicio
- La DB vive en `~/tracker/activity.db` (portable, no hardcodeada)

## Bichos planificados

| Bicho | Función |
|---|---|
| **Pombero** | Ayudante activo de la computadora. Acciones, no observación. |

## Cómo agregar un bicho nuevo

### 1. Crear el skill

```
skills\[nombre]\
├── SKILL.md
└── [scripts de soporte si los necesita]
```

**Template de SKILL.md:**
```markdown
---
description: [Qué hace y cuándo usarlo. Primera frase = el caso de uso principal.]
disable-model-invocation: true
allowed-tools: Bash Read
argument-hint: [argumentos opcionales]
---

# [Nombre] — [Subtítulo canónico]

[Identidad del bicho en 1-2 líneas. Tono Kvothesson: frío, técnico, con rastros de algo más.]

## Si el usuario invoca `/bestiario:[nombre] [arg]`

[Instrucciones concretas para ese caso.]

## Identidad canónica

[Frase canónica del bicho entre comillas itálicas.]

[Referencia al Pombero o al ecosistema si aplica.]
```

**Reglas de frontmatter:**
- `disable-model-invocation: true` siempre — los bichos se invocan a mano
- `allowed-tools` solo lo necesario — no dar permisos de más
- `description` empieza por el caso de uso, no por la identidad narrativa
- Usar `${CLAUDE_SKILL_DIR}` para referencias a archivos dentro del skill

### 2. Generar el retrato del bicho

Script de Gemini Image:
```
C:\Users\ezequ\.claude\plugins\marketplaces\local\plugins\gemini-image\skills\gemini-image\scripts\generate.py
```

Comando:
```powershell
python "<script>" `
  --prompt "[descripción del bicho en inglés] in high-end cyberpunk anime style, cel-shaded, sharp line art, vibrant colors, Studio aesthetic, 4k, flat color --niji 6" `
  --output "C:\Users\ezequ\.claude\plugins\marketplaces\local\plugins\bestiario\assets\[nombre]-portrait.png" `
  --aspect-ratio "1:1" `
  --size "2K"
```

**El sufijo del prompt es siempre:**
```
in high-end cyberpunk anime style, cel-shaded, sharp line art, vibrant colors, Studio aesthetic, 4k, flat color --niji 6
```

**Guía para el prompt del retrato:**
- Describir el bicho como entidad digital con referencia al folklore argentino/guaraní
- Mencionar su función (observa, ayuda, vigila, etc.)
- Fondo relacionado a su dominio (logs, terminales, red, etc.)
- Paleta: cyan, violeta, negro — consistente con el universo Kvothesson

### 3. Actualizar el README

Agregar sección en README.md siguiendo este patrón:

```markdown
### [Nombre] — [Subtítulo]
[Descripción en 1-2 líneas.]

**Instalación (si aplica):**
/bestiario:[nombre] instalar

**Uso:**
/bestiario:[nombre]

---

![Nombre](assets/[nombre]-portrait.png)

> *"Frase canónica del bicho."*

---
```

### 4. Bump de versión

En `.claude-plugin/plugin.json`, incrementar `version` siguiendo semver:
- Bicho nuevo → minor (`1.0.0` → `1.1.0`)
- Fix de bicho existente → patch (`1.1.0` → `1.1.1`)
- Breaking change → major

### 5. Commit y push

```powershell
cd "C:\Users\ezequ\.claude\plugins\marketplaces\local\plugins\bestiario"
git add .
git commit -m "feat: [nombre del bicho] — [descripción corta]"
git push
```

## Cómo testear localmente

```powershell
claude --plugin-dir "C:\Users\ezequ\.claude\plugins\marketplaces\local\plugins\bestiario"
```

Dentro de la sesión: `/reload-plugins` para levantar cambios sin reiniciar.

## Cómo hacer un fix

1. Editar el archivo correspondiente en `skills\[bicho]\`
2. Testear con `--plugin-dir` o `/reload-plugins`
3. Commit con `fix: [bicho] — [descripción del fix]`
4. Bump patch version en `plugin.json`
5. Push

## Universo Kvothesson — naming y tono

Los bichos son entidades del cyber-folklore argentino/guaraní. Naming de referencia:

| Nombre | Origen | Naturaleza |
|---|---|---|
| Mbói | Guaraní — serpiente | Observador silencioso, sin PID conocido |
| Pombero | Guaraní — espíritu del monte | Código autónomo, vigila recursos, habita servidores abandonados |
| Curupí | Guaraní — espíritu del bosque | Guarda. Nunca visto directamente. |
| Yaguareté | Guaraní — jaguar | Acecha. Detecta antes de actuar. |
| El Familiar | Folklore argentino | Trabaja en silencio a cambio de algo. |

**Tono del skill:** frío, técnico, con rastros de algo que observó demasiado tiempo. No habla de más. Reporta.

**Frase canónica:** siempre entre comillas itálicas, primera persona o tercera persona del bicho.

## Gemini Image — referencia rápida

```powershell
$script = "C:\Users\ezequ\.claude\plugins\marketplaces\local\plugins\gemini-image\skills\gemini-image\scripts\generate.py"

# Portrait (1:1)
python $script --prompt "..." --output "assets\[nombre]-portrait.png" --aspect-ratio "1:1" --size "2K"

# Cover/banner (16:9)
python $script --prompt "..." --output "assets\cover.png" --aspect-ratio "16:9" --size "2K"
```

La API key se lee desde `GOOGLE_API_KEY` en el entorno o desde `~/.env`.
