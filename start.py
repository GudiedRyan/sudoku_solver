import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
frontend = root / "frontend"
backend = root / "backend"

npm = "npm.cmd" if sys.platform == "win32" else "npm"

subprocess.run([npm, "run", "build"], cwd=frontend, check=True)
subprocess.run([sys.executable, "app.py"], cwd=backend, check=True)
