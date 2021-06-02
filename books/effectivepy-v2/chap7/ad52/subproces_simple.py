"""

"""

import subprocess

result = subprocess.run(
    ["echo", "Hello from the child"],
    capture_output=True,
    encoding="utf-8",
)

result.check_returncode()
print(result.stdout)
