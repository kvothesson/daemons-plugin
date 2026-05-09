import sqlite3
import sys
import os
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DB_PATH = os.path.join(os.path.expanduser("~"), "tracker", "activity.db")

if not os.path.exists(DB_PATH):
    print(f"DB no encontrada en {DB_PATH}. Ejecutá /bestiario:mboi instalar primero.")
    sys.exit(1)

conn = sqlite3.connect(DB_PATH)

print("=== TIEMPO TOTAL POR APP ===")
for r in conn.execute("""
    SELECT app, COUNT(*) as switches, SUM(duration_sec) as total_sec
    FROM activity GROUP BY app ORDER BY total_sec DESC LIMIT 15
"""):
    print(f"{r[0]:<25} {r[1]:>5} switches   {r[2]//60:>5} min")

print("\n=== SECUENCIAS FRECUENTES ===")
rows = conn.execute("SELECT app, title, duration_sec FROM activity ORDER BY id").fetchall()
transitions = defaultdict(int)
for i in range(len(rows) - 1):
    a, b = rows[i][0], rows[i+1][0]
    if a != b:
        transitions[(a, b)] += 1
for (a, b), count in sorted(transitions.items(), key=lambda x: -x[1])[:15]:
    print(f"{a:<20} -> {b:<20}  {count:>4}x")

print("\n=== FRAGMENTACION EXTREMA < 10s ===")
for r in conn.execute("""
    SELECT app, title, COUNT(*) as hits FROM activity
    WHERE duration_sec < 10
    GROUP BY app, title ORDER BY hits DESC LIMIT 15
"""):
    print(f"{r[2]:>4}x  {r[0]:<20}  {r[1][:50]}")

print("\n=== BUSQUEDAS EN BROWSER ===")
for r in conn.execute("""
    SELECT title, COUNT(*) as hits FROM activity
    WHERE (app LIKE '%chrome%' OR app LIKE '%firefox%' OR app LIKE '%msedge%')
    AND title NOT LIKE '%localhost%' AND duration_sec > 5
    GROUP BY title ORDER BY hits DESC LIMIT 20
"""):
    print(f"{r[1]:>4}x  {r[0][:70]}")

conn.close()
