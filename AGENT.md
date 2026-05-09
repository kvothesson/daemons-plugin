# Bestiario — Contexto de desarrollo

Plugin de Claude Code del universo Kvothesson. Cada bicho es un skill con identidad propia.

---

## Regla fundamental: plataforma agnóstica

**Los bichos son entidades del cyber-folklore, no de un sistema operativo.**

Deben poder ejecutarse en cualquier entorno donde corra Claude Code: Windows, macOS, Linux, ARM, lo que sea.

**Reglas:**

- Detectar el OS al inicio con `platform.system()` (Python) o `uname -s` (shell)
- Nunca hardcodear rutas del sistema (`C:\Windows`, `/usr/local/`, etc.)
- Usar Python con `psutil`, `pathlib`, `shutil` como capa cross-platform siempre que sea posible
- Para comandos nativos que difieren por OS: branch explícito, una rama por plataforma
- Rutas de usuario: `Path.home()` en Python, `~` en shell
- Si una función no existe en un OS dado: decirlo en una línea, no fallar silenciosamente
- Scripts de soporte dentro del skill: referenciar con `${CLAUDE_SKILL_DIR}/script.py`

**Patrón de detección:**

```python
import platform
os_name = platform.system()  # 'Windows' | 'Darwin' | 'Linux'

if os_name == "Windows":
    ...
elif os_name == "Darwin":
    ...
elif os_name == "Linux":
    ...
else:
    print(f"Plataforma {os_name} no soportada aún.")
```

---

## Reglas antes de commitear

Antes de cualquier `git add` o `git commit`, verificar que ningún archivo contiene:

- Rutas absolutas con nombre de usuario (`C:\Users\[nombre]\`, `/home/[nombre]/`)
- Paths a archivos `.env`, claves, tokens o credenciales
- Nombres de máquinas, organizaciones internas o datos de red

**Regla práctica:** si una ruta no funcionaría en la máquina de otra persona, no va al repo.

**Cómo reemplazar:**

| En vez de... | Usar... |
|---|---|
| `C:\Users\<nombre>\alguna\carpeta\` | `Path.home() / "alguna/carpeta"` o `~` |
| Path a un `.env` personal | `~/.env` o variable de entorno documentada |
| Path hardcodeado a script del plugin | `${CLAUDE_SKILL_DIR}/script.py` |

Verificar antes del commit:

```bash
git diff --cached | grep -iE "Users/|Users\\\\|/home/[a-z]|\.env|api.key"
```

---

## Repo y estructura

```
bestiario-plugin/
├── .claude-plugin/
│   └── plugin.json          ← metadata + version (bumpar al hacer release)
├── assets/                  ← imágenes para el README
│   ├── cover.png
│   └── [bicho]-portrait.png
├── skills/
│   └── [nombre-bicho]/
│       ├── SKILL.md         ← el bicho en sí
│       └── [scripts de soporte si los necesita]
├── README.md
└── AGENT.md                 ← este archivo
```

GitHub: https://github.com/kvothesson/bestiario-plugin

---

## Bichos existentes

| Bicho | Skill | Función |
|---|---|---|
| Mbói | `/bestiario:mboi` | Observador silencioso. Rastrea actividad, detecta fricciones. |
| Pombero | `/bestiario:pombero` | Técnico del sistema. Diagnostica, mantiene y repara. |

**Mbói — contexto adicional:**
- El tracker (`~/tracker/tracker.py`) corre en background y graba actividad de ventanas en SQLite
- Detección de ventana activa: pywin32 (Windows), osascript (macOS), xdotool (Linux)
- Autostart: Startup folder (Windows), LaunchAgent (macOS), .config/autostart (Linux)
- La DB vive en `~/tracker/activity.db`

**Pombero — contexto adicional:**
- Usa `psutil` como capa principal (cross-platform)
- Ramas nativas por OS solo donde psutil no alcanza (temperatura, etc.)

---

## Cómo agregar un bicho nuevo

### 1. Crear el skill

```
skills/[nombre]/
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

## Detección de plataforma

Antes de cualquier acción, detectar el OS:

```python
import platform
os_name = platform.system()
```

## Si el usuario invoca `/bestiario:[nombre] [arg]`

[Instrucciones concretas, con ramas por OS donde corresponda.]

## Identidad canónica

[Frase canónica del bicho entre comillas itálicas.]
```

**Reglas de frontmatter:**
- `disable-model-invocation: true` siempre — los bichos se invocan a mano
- `allowed-tools` solo lo necesario — no dar permisos de más
- `description` empieza por el caso de uso, no por la identidad narrativa
- Usar `${CLAUDE_SKILL_DIR}` para referencias a archivos dentro del skill

### 2. Generar el retrato del bicho

Comando (ajustar paths según el entorno):

```bash
python path/to/gemini-image/generate.py \
  --prompt "[descripción] in high-end cyberpunk anime style, cel-shaded, sharp line art, vibrant colors, Studio aesthetic, 4k, flat color --niji 6" \
  --output "assets/[nombre]-portrait.png" \
  --aspect-ratio "1:1" \
  --size "2K"
```

**El sufijo del prompt es siempre:**
```
in high-end cyberpunk anime style, cel-shaded, sharp line art, vibrant colors, Studio aesthetic, 4k, flat color --niji 6
```

**Guía para el prompt del retrato:**
- Describir el bicho como entidad digital con referencia al folklore argentino/guaraní
- Mencionar su función (observa, diagnostica, vigila, etc.)
- Fondo relacionado a su dominio (logs, terminales, red, hardware, etc.)
- Paleta: cyan, violeta, negro — consistente con el universo Kvothesson

### 3. Actualizar el README

```markdown
### [Nombre] — [Subtítulo]
[Descripción en 1-2 líneas.]

**Uso:**
/bestiario:[nombre]

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

```bash
cd bestiario-plugin/
git add .
git commit -m "feat: [nombre del bicho] — [descripción corta]"
git push
```

---

## Cómo testear localmente

```bash
claude --plugin-dir path/to/bestiario-plugin
```

Dentro de la sesión: `/reload-plugins` para levantar cambios sin reiniciar.

---

## Universo Kvothesson — naming y tono

Los bichos son entidades del cyber-folklore argentino/guaraní. Naming de referencia:

| Nombre | Origen | Naturaleza |
|---|---|---|
| Mbói | Guaraní — serpiente | Observador silencioso, sin PID conocido |
| Pombero | Guaraní — espíritu del monte | Técnico. Conoce cada rincón del sistema. |
| Curupí | Guaraní — espíritu del bosque | Guarda. Nunca visto directamente. |
| Yaguareté | Guaraní — jaguar | Acecha. Detecta antes de actuar. |
| El Familiar | Folklore argentino | Trabaja en silencio a cambio de algo. |

**Tono del skill:** frío, técnico, con rastros de algo que observó demasiado tiempo. No habla de más. Reporta.

**Frase canónica:** siempre entre comillas itálicas, primera o tercera persona del bicho.
