"""

"""
import subprocess
import time

start = time.time()
sleep_procs = []

for _ in range(10):
    proc = subprocess.Popen(["sleep", "1"])
    sleep_procs.append(proc)


for proc in sleep_procs:
    proc.communicate()


end = time.time()
delta = end - start
print(f"Finished in {delta:.3} seconds")

