import time
import sqlite3
import signal
import sys
import os
from datetime import datetime

try:
    import win32gui
    import win32process
    import psutil
except ImportError:
    print("Instalá dependencias: pip install pywin32 psutil")
    sys.exit(1)

DB_PATH = os.path.join(os.path.dirname(__file__), "activity.db")
MIN_DURATION_SEC = 2  # ignora flickers


def get_active_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        app = psutil.Process(pid).name().replace(".exe", "").lower()
        return app, title
    except Exception:
        return None, None


def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS activity (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp     TEXT    NOT NULL,
            app           TEXT,
            title         TEXT,
            duration_sec  INTEGER
        )
    """)
    conn.commit()


def main():
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    current_app = None
    current_title = None
    start_time = None

    def flush():
        if current_app and start_time:
            duration = int(time.time() - start_time)
            if duration >= MIN_DURATION_SEC:
                conn.execute(
                    "INSERT INTO activity (timestamp, app, title, duration_sec) VALUES (?, ?, ?, ?)",
                    (datetime.fromtimestamp(start_time).isoformat(), current_app, current_title, duration),
                )
                conn.commit()

    def on_exit(sig, frame):
        flush()
        conn.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, on_exit)
    signal.signal(signal.SIGTERM, on_exit)

    print(f"Tracker corriendo. DB: {DB_PATH}  |  Ctrl+C para detener.")

    while True:
        app, title = get_active_window()

        if app != current_app or title != current_title:
            flush()
            current_app = app
            current_title = title
            start_time = time.time()

        time.sleep(1)


if __name__ == "__main__":
    main()
