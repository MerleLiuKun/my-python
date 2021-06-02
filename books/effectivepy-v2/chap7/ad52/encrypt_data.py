"""

"""

import os
import subprocess


def run_encrypt(data):
    env = os.environ.copy()
    env["password"] = "zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1"
    proc = subprocess.Popen(
        ["openssl", "enc", "-des3", "-pass", "env:password"],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


# procs = []
# for _ in range(3):
#     data = os.urandom(10)
#     proc = run_encrypt(data)
#     procs.append(proc)
#
# for proc in procs:
#     out, _ = proc.communicate()
#     print(out[-10:])


def run_hash(input_stdin):
    return subprocess.Popen(
        ["openssl", "dgst", "-whirlpool", "-binary"],
        stdin=input_stdin,
        stdout=subprocess.PIPE,
    )


encrypt_procs = []
hash_procs = []

for _ in range(10):
    data = os.urandom(100)

    e_proc = run_encrypt(data)
    encrypt_procs.append(e_proc)

    h_proc = run_hash(e_proc.stdout)
    hash_procs.append(h_proc)

    e_proc.stdout.close()
    e_proc.stdout = None

for proc in encrypt_procs:
    proc.communicate()
    assert proc.returncode == 0

for proc in hash_procs:
    out, _ = proc.communicate()
    print(out[-10:])
    assert proc.returncode == 0
