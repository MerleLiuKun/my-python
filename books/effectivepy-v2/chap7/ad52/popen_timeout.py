"""

"""
import subprocess

proc = subprocess.Popen(
    ["sleep", "10"]
)

try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print("Exit")
