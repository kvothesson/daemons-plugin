# Bichos — Catálogo y contexto

Referencia completa de todos los bichos activos del bestiario.

---

## Tabla de bichos

| Bicho | Skill | Función |
|---|---|---|
| Mbói | `/bestiario:mboi` | Observador silencioso. Rastrea actividad de ventanas, detecta fricciones y oportunidades de automatización. |
| Pombero | `/bestiario:pombero` | Técnico del sistema. Diagnostica hardware, rendimiento, disco, red y temperatura. |
| Añá | `/bestiario:ana` | Probador de resiliencia. Simula condiciones adversas (red cortada, disco lleno, proceso zombi). |
| Irupé | `/bestiario:irupe` | Organizador de archivos acumulados. Propone estructura sin mover nada hasta que el usuario confirme. |
| Ka'a Yarýi | `/bestiario:kaayaryi` | Guardián del tiempo de trabajo. Rastrea sesiones de foco y detecta cuándo el rendimiento cae. |
| Lobizón | `/bestiario:lobizon` | Cambiador de contexto. Guarda y restaura entornos completos (vars, directorio, notas) entre proyectos. |
| Luz Mala | `/bestiario:luzmala` | Monitor de anomalías silencioso. Detecta picos de red, procesos nuevos y cambios inesperados. |
| Mainumby | `/bestiario:mainumby` | Buscador web rápido. Busca, lee fuentes y devuelve lo esencial sin browser ni distracción. |

---

## Contexto por bicho

**Mbói**
- El tracker (`~/tracker/tracker.py`) corre en background y graba actividad de ventanas en SQLite
- Detección de ventana activa: pywin32 (Windows), osascript (macOS), xdotool (Linux)
- Autostart: Startup folder (Windows), LaunchAgent (macOS), .config/autostart (Linux)
- La DB vive en `~/tracker/activity.db`

**Pombero**
- Usa `psutil` como capa principal (cross-platform)
- Ramas nativas por OS solo donde psutil no alcanza (temperatura, etc.)

**Añá**
- Solo simula — nunca borra datos reales
- Siempre puede revertirse con `/bestiario:ana restaurar`
- Args: `red | proceso | disco | listar | restaurar`

**Irupé**
- Carpetas por defecto según plataforma (Descargas, Escritorio, Temp)
- Propone estructura, espera confirmación antes de mover nada
- Args: `analizar | organizar <carpeta> | limpiar-temp`

**Ka'a Yarýi**
- Guarda sesiones en SQLite local (`~/kaayaryi/sessions.db`)
- Detecta caída de foco comparando tiempo activo vs tiempo transcurrido
- Args: `inicio | fin | estado | hoy`

**Lobizón**
- Persiste contextos en `~/lobizon/contexts/`
- Cada contexto guarda: variables de entorno, directorio activo, notas libres
- Args: `listar | guardar <nombre> | cargar <nombre> | borrar <nombre>`

**Luz Mala**
- Toma snapshot al invocar y compara contra baseline anterior
- Detecta: conexiones de red nuevas, procesos que aparecieron, notificaciones acumuladas
- Args: `red | procesos | todo`

**Mainumby**
- `allowed-tools` incluye `WebSearch` y `WebFetch` — único bicho con acceso a internet
- Lee 2-3 fuentes, devuelve respuesta estructurada con fuentes al pie
- No comenta lo que no le preguntaron