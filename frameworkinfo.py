#!/usr/bin/env python
import subprocess
import shutil

# depends on pciutils, dmidecode, lshw

def check_installed(program):
    return shutil.which(program)

# Run the commands and store their output in variables
try:
    if check_installed("dmidecode"):
        bios_info = subprocess.check_output("sudo dmidecode | grep -A3 'Vendor:'", shell=True)
        system_info = subprocess.check_output("sudo dmidecode | grep -A7 'System Information'", shell=True)
except subprocess.CalledProcessError:
    print("dmidecode is not installed")

try:
    if check_installed("lshw"):
        cpu_info = subprocess.check_output("sudo lshw -C cpu | grep -A3 'product:'", shell=True)
except subprocess.CalledProcessError:
    print("lshw is not installed")

try:
    if check_installed("uname"):
        kernel_version = subprocess.check_output("uname -r", shell=True)
except subprocess.CalledProcessError:
    print("uname is not installed")


# Print outout to shell
print(f"{system_info.decode()}")
print(f"BIOS info:\n{bios_info.decode()}")
print(f"CPU info:\n{cpu_info.decode()}")
print(f"Kernel version: {kernel_version.decode()}")
