# Bestiario — Plugin de Claude Code

![Bestiario Cover](assets/cover.png)

Bichos digitales del universo Kvothesson. Observan, detectan, actúan. Corren sin PID conocido.

## Instalación

```
/plugin install https://github.com/kvothesson/bestiario-plugin
```

---

## Bichos disponibles

---

### Mbói — El Observador

Rastrea tu actividad en la computadora y detecta fricciones, flujos repetitivos y oportunidades para plugins, agentes o MCPs. No interviene — observa y reporta.

Instala un tracker silencioso que registra qué apps usás y cuánto tiempo. Cuando tenés datos acumulados, lo invocás y te dice qué patrones encontró.

**Instalar tracker:**
```
/bestiario:mboi instalar
```

**Analizar (con datos acumulados):**
```
/bestiario:mboi
```

<details>
<summary><strong>Ver ejemplo de output</strong></summary>

```
=== TIEMPO TOTAL POR APP ===
vscode                       142 switches     310 min
chrome                       198 switches     180 min
slack                         89 switches      95 min
terminal                      54 switches      40 min
notion                        23 switches      28 min
figma                          9 switches      12 min

=== SECUENCIAS FRECUENTES ===
vscode               -> chrome                  42x
chrome               -> vscode                  39x
vscode               -> terminal                28x
terminal             -> vscode                  27x
slack                -> chrome                  21x
chrome               -> slack                   18x

=== FRAGMENTACION EXTREMA < 10s ===
  31x  chrome     Nueva pestaña - Google Chrome
  18x  vscode     Welcome — Visual Studio Code
  14x  slack      Slack | mensajes directos
  11x  terminal   bash

=== BUSQUEDAS EN BROWSER ===
  12x  typescript generics extends keyof - Google
   9x  react useEffect cleanup - Google
   8x  prisma relations many to many - Google
   6x  Stack Overflow - Google Chrome
   5x  How to center a div - Google
```

**Output del análisis:**

```
[CANDIDATO 1]
Patrón:    vscode → chrome → vscode repetido 42 veces por día, 5 días seguidos
Fricción:  buscás documentación afuera del editor constantemente
Hipótesis: MCP de documentación inline (DevDocs, MDN) o Copilot Chat integrado
Evidencia: 42 transiciones/día × 5 días = 210 interrupciones de flujo
Mercado:   Todo desarrollador. Problema universal.

[CANDIDATO 2]
Patrón:    "Nueva pestaña" fragmentada 31 veces en < 10s
Fricción:  Abrís Chrome sin saber a dónde vas. Hay algo que no está donde debería.
Hipótesis: Falta un launcher o un panel de accesos rápidos
Evidencia: 31 hits de fragmentación extrema
Mercado:   Desarrolladores con flujo caótico de referencias

[CANDIDATO 3]
Patrón:    "typescript generics" buscado 12 veces en 5 días
Fricción:  Conocimiento que no se queda. Siempre volvés a buscarlo.
Hipótesis: Plugin de snippets o cheatsheet local con búsqueda rápida
Evidencia: 12 búsquedas repetidas de la misma query
Mercado:   Devs de TypeScript. Millones.
```

</details>

![Mbói](assets/mboi-portrait.png)

> *"El Mbói no tiene forma fija. Es el patrón antes de que el patrón tenga nombre."*

---

### Pombero — El Técnico

Diagnostica, mantiene y repara tu sistema. Salud del hardware, rendimiento, disco, red, memoria, temperatura. Funciona en Windows, macOS y Linux.

```
/bestiario:pombero [diagnosticar | disco | red | memoria | temperatura | reparar]
```

<details>
<summary><strong>Ver ejemplo — <code>diagnosticar</code></strong></summary>

```
ESTADO DEL SISTEMA — 2026-05-09 14:32
OS:        macOS 14.4 Sonoma
CPU:       8 cores — 12% uso actual
           Frecuencia: 3200 MHz
Memoria:   11.4 GB libres de 16.0 GB (28.8% usado)
Swap:      0.0 GB usado de 2.0 GB
Uptime:    2d 6h 14m

Disco /:    142.3 GB libres de 494.4 GB — OK
Disco /data: 12.1 GB libres de 500.0 GB — ATENCIÓN

Temperaturas:
  cpu/CPU Core 0: 48°C
  cpu/CPU Core 1: 51°C
  ssd/Drive Temp: 38°C

Errores recientes (1h): Ninguno
```

</details>

<details>
<summary><strong>Ver ejemplo — <code>disco</code></strong></summary>

```
DISCOS:

  /dev/sda1 (ext4) -> /
  Total: 494.4 GB | Usado: 352.1 GB | Libre: 142.3 GB | OK

  /dev/sdb1 (ext4) -> /data
  Total: 500.0 GB | Usado: 487.9 GB | Libre: 12.1 GB | ATENCIÓN

Top carpetas en home:
  ~/Videos:        48.30 GB
  ~/Documents:     22.10 GB
  ~/Downloads:     18.74 GB
  ~/dev:           11.20 GB
  ~/.local:         5.43 GB
  ~/Pictures:       3.87 GB

Temp (/tmp): 1240 MB
  ATENCIÓN: más de 1 GB en temp
```

</details>

<details>
<summary><strong>Ver ejemplo — <code>memoria</code></strong></summary>

```
RAM:  16.0 GB total | 11.4 GB libre | 28.8% usado
Swap: 2.0 GB total | 0.0 GB usado

Top procesos por memoria:
  firefox                             PID 3821: 1240 MB
  Xorg                                PID 1204:  480 MB
  code                                PID 5530:  412 MB
  slack                               PID 6102:  388 MB
  spotify                             PID 7841:  201 MB
  python3                             PID 9012:  144 MB
  node                                PID 4401:  138 MB
  postgres                            PID 1890:   92 MB
```

</details>

<details>
<summary><strong>Ver ejemplo — <code>reparar</code></strong></summary>

```
1. Temp limpiado: 847 archivos eliminados
2. Caché DNS limpiado (Linux)
3. Limpiando paquetes huérfanos...
   apt: hecho — 340 MB liberados

Reparación completa.
```

</details>

![Pombero](assets/pombero-portrait.png)

> *"Ya sabía lo que iba a encontrar. Lo que cambia es cuándo te lo cuento."*

---

### Mainumby — El Colibrí Digital

Buscador web rápido y preciso. Le preguntás algo del mundo exterior, entra, toma lo esencial y sale. Sin browser, sin distracción, sin preámbulo.

```
/bestiario:mainumby <consulta>
```

<details>
<summary><strong>Ver ejemplo de output</strong></summary>

```
[MAINUMBY]
Consulta: precio dolar blue hoy argentina
Fuente:   https://dolarhoy.com

Dólar blue: $1.285 compra / $1.305 venta (09/05/2026 14:30)
Brecha con oficial: 21.4%
Sin variación significativa respecto a ayer.

Otras fuentes:
- https://ambito.com — confirma mismo valor, agrega contexto de reservas del BCRA
- https://infobae.com — nota sobre estabilización post-acuerdo FMI
```

</details>

![Mainumby](assets/mainumby-portrait.png)

> *"Estuvo. Buscó. Ya no está."*

---

### Ka'a Yarýi — El Espíritu de la Yerba

Guardián del tiempo de trabajo. Rastrea sesiones de foco, mide cuánto tiempo llevás, detecta cuándo el bloque fue demasiado largo. No da consejos — muestra el número.

```
/bestiario:kaayaryi [inicio|fin|estado|hoy]
```

<details>
<summary><strong>Ver ejemplo de output</strong></summary>

```
/bestiario:kaayaryi inicio
[KA'A YARÝI] Sesión iniciada: 09:14
El mate está listo. El tiempo corre.

/bestiario:kaayaryi estado
[KA'A YARÝI] En sesión desde 09:14 — 47 min transcurridos.

/bestiario:kaayaryi fin
[KA'A YARÝI] Sesión cerrada: 112 min. Largo. Considerá un descanso antes del siguiente.

/bestiario:kaayaryi hoy
[KA'A YARÝI] Hoy — 09/05/2026
Sesiones: 3 completadas
Tiempo total: 287 min (4.8 hs)
  · 09:14 — 112 min
  · 14:02 — 98 min
  · 17:30 — 77 min
```

</details>

![Ka'a Yarýi](assets/kaayaryi-portrait.png)

> *"Sabe cuánto tiempo llevás. No lo dice hasta que preguntás."*

---

### El Lobizón — El que se Transforma

Cambiador de contexto de trabajo. Guarda y restaura entornos: directorio activo, variables de entorno, notas de proyecto. Útil para alternar entre proyectos, clientes o roles.

```
/bestiario:lobizon [listar|guardar <nombre>|cargar <nombre>|borrar <nombre>]
```

<details>
<summary><strong>Ver ejemplo de output</strong></summary>

```
/bestiario:lobizon listar
[LOBIZÓN] Contextos disponibles:
  · cliente-acme    — Branch activo: feature/payments. Contacto: maria@acme.com
  · proyecto-x      — Staging env. Reunión viernes.
  · personal        — side projects, sin deadline

/bestiario:lobizon cargar cliente-acme
[LOBIZÓN] Cargando 'cliente-acme'...
  Directorio: /home/user/dev/acme-backend
  Variables de entorno a setear:
    export ENV=staging
    export API_URL=https://staging.acme.com
    export DB_NAME=acme_staging
  Notas: Branch activo: feature/payments. Contacto: maria@acme.com

  Copiá los exports de arriba y ejecutalos en tu shell.
  El directorio lo podés cambiar con: cd /home/user/dev/acme-backend
```

</details>

![El Lobizón](assets/lobizon-portrait.png)

> *"No es el mismo que era antes. Tampoco recuerda haberlo sido."*

---

### La Luz Mala — El Fuego Fatuo

Monitor silencioso de anomalías del entorno. Ve qué pasó mientras no mirabas: picos de red, procesos nuevos, conexiones inesperadas. No avisa si no hay nada. Aparece cuando algo no cuadra.

```
/bestiario:luzmala [red|procesos|todo]
```

<details>
<summary><strong>Ver ejemplo de output</strong></summary>

```
/bestiario:luzmala todo
[LUZ MALA] Red — 14:32:07
Conexiones establecidas: 34
  · chrome:           18 conexiones — 142.250.80.1, 216.58.202.46
  · node:              8 conexiones — 127.0.0.1
  · slack:             5 conexiones — 44.238.171.5
  · python:            3 conexiones — 52.94.236.248

Tráfico total sesión:
  Enviado:    84.3 MB
  Recibido:  412.7 MB

[LUZ MALA] Procesos — 14:32:08
Top CPU:
  · node                         CPU: 34.2%  RAM: 2.1%
  · chrome                       CPU:  8.7%  RAM: 4.8%

Iniciados en los últimos 30 min:
  · [14:11] python3
  · [14:08] node
  · [14:03] postgres

Anomalías detectadas:
  · node con CPU > 30% sostenido — posible loop o build colgado
```

</details>

![La Luz Mala](assets/luzmala-portrait.png)

> *"Nadie la llama. Llega igual. Siempre donde no debería haber nada."*

---

### Irupé — La Flor del Agua

Organizador de archivos acumulados. Analiza descargas y escritorio, agrupa por tipo y fecha, propone estructura. No mueve nada hasta que el usuario confirme.

```
/bestiario:irupe [analizar|organizar <carpeta>|limpiar-temp]
```

<details>
<summary><strong>Ver ejemplo de output</strong></summary>

```
/bestiario:irupe analizar
[IRUPÉ] Análisis de archivos acumulados

Total: 374 archivos en Downloads y Desktop

  .png                 143 archivos  (1034.5 MB)  125 de más de 30 días
  .mp4                  64 archivos  ( 934.6 MB)   54 de más de 30 días
  .mp3                  36 archivos  ( 199.8 MB)   34 de más de 30 días
  .sfk                  27 archivos  (   0.8 MB)   27 de más de 30 días
  .pdf                  19 archivos  (  10.6 MB)    6 de más de 30 días
  ...

Para organizar: /bestiario:irupe organizar Downloads

/bestiario:irupe organizar Downloads
[IRUPÉ] Plan de organización: Downloads
(nada se mueve hasta que confirmes)

  imagenes/     (167 archivos, 1035.5 MB)
    · 01.png
    · 02.png
    · ... y 165 más
  video/         (64 archivos, 934.7 MB)
  audio/         (41 archivos, 318.9 MB)
  documentos/    (33 archivos,   5.0 MB)
  instaladores/   (4 archivos,  57.8 MB)

Si querés que lo haga: confirmá con 'sí, organizá'
```

</details>

![Irupé](assets/irupe-portrait.png)

> *"Está quieta. El orden llega a ella, no al revés."*

---

### Añá — El Espíritu del Mal

Probador de resiliencia del entorno. Simula condiciones adversas: corte de red, proceso de alta CPU, disco lleno. Para descubrir qué tan frágil es lo que construiste antes de que lo descubra solo.

```
/bestiario:ana [listar|red|proceso|disco|restaurar]
```

<details>
<summary><strong>Ver ejemplo de output</strong></summary>

```
/bestiario:ana listar
[AÑÁ] Pruebas disponibles:
  red      — simular pérdida de conectividad (bloquear DNS por 60s)
  proceso  — crear proceso zombi de alta CPU por 30s
  disco    — crear archivo de 500MB en /tmp para simular disco lleno
  restaurar — revertir todas las simulaciones activas

/bestiario:ana proceso
[AÑÁ] Proceso de alta CPU iniciado por 30 segundos.
Observá el comportamiento de tu sistema.
[AÑÁ] Proceso finalizado.

/bestiario:ana red
[AÑÁ] DNS bloqueado por 60 segundos. Observá qué falla.
Para restaurar antes: /bestiario:ana restaurar

/bestiario:ana restaurar
[AÑÁ] Archivo de disco eliminado.
[AÑÁ] Simulaciones revertidas. El entorno volvió a la normalidad.
```

</details>

![Añá](assets/ana-portrait.png)

> *"No es el mal. Es lo que el mal haría. La diferencia importa."*

---
