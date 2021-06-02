"""

"""
import subprocess
import time

proc = subprocess.Popen(["sleep", "1"])

while proc.poll() is None:
    print("Working...")
    time.sleep(1)  # 模拟其他任务处理

print(f"Exit status {proc.poll()}")
