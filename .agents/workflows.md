# Workflows — Agregar un bicho nuevo

---

## Checklist completo

### 1. Crear el skill

```
skills/[nombre]/
├── SKILL.md
└── [scripts de soporte si los necesita]
```

Seguir el template en `.agents/skills.md`.

### 2. Generar el retrato del bicho

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

**Guía para el prompt:**
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

### 4. Actualizar `.agents/bichos.md`

Agregar fila en la tabla y bloque de contexto adicional.

### 5. Actualizar `plugin.json`

Agregar entry en el array `skills`:

```json
{
  "name": "[nombre]",
  "path": "skills/[nombre]/SKILL.md"
}
```

### 6. Bump de versión en `plugin.json`

Semver:
- Bicho nuevo → minor (`1.7.0` → `1.8.0`)
- Fix de bicho existente → patch (`1.7.0` → `1.7.1`)
- Breaking change → major

### 7. Verificar antes de commitear

```bash
git diff --cached | grep -iE "Users/|Users\\|/home/[a-z]|\.env|api.key"
```

### 8. Commit y push

```bash
git add .
git commit -m "feat: [nombre del bicho] — [descripción corta]"
git push
```

---

## Testear localmente

```bash
claude --plugin-dir path/to/bestiario-plugin
```

Dentro de la sesión: `/reload-plugins` para levantar cambios sin reiniciar.