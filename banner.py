#!/usr/bin/env python
""" Module to display banner on login """
from __future__ import print_function
import os
import sys
import platform
import subprocess
from util import distro


def print_horizontal_line(count=10):
    """ Print gradient blue horizontal line """
    for x in range(0, count):
        for i in range(18, 22):
            print("\033[48;5;" + str(i) + "m \033[0m", end='')
        for i in range(21, 17, -1):
            print("\033[48;5;" + str(i) + "m \033[0m", end='')
    print('')


def print_vert_line(mode=0):
    """ Print either opening or closing vertical line """
    if mode == 0:
        print("\033[48;5;18m \033[0m\033[48;5;19m \033[0m", end=' ')
    else:
        print("\033[48;5;19m \033[0m\033[48;5;18m \033[0m")


def print_padded_string(value, pad=75):
    """ print padded with spaces string """
    print(value.ljust(pad), end='')


def print_hostname():
    """ Print Hostname """
    print_padded_string('Hostname: ' + platform.node())


def print_release():
    """ print Release Information """
    if platform.system() == "Linux":
        if os.path.exists('/etc/system-release'):
            with open('/etc/system-release', 'r') as sysrel:
                release = sysrel.read()
                release = release.replace('\n', '')
            print_padded_string('Release: ' + release)
        else:
            print_padded_string('Release: ' + " ".join(distro.linux_distribution()))
    elif platform.system() == "Darwin":
        print_padded_string('Release: macOS ' + platform.mac_ver()[0])
    else:
        print_padded_string('Release: N/A')


def print_kernel_info(mode=0):
    """ Print Kernel Information """
    if platform.system() == "Linux":
        if mode == 0:
            cmd = ['uname', '-r']
            stdout = subprocess.check_output(cmd)
            kernel = stdout.replace('\n', '')
            print_padded_string("Kernel: " + kernel)
        if mode == 1:
            cmd = ['uname', '-v']
            stdout = subprocess.check_output(cmd)
            version = stdout.replace('\n', '')
            print_padded_string("Build: " + version)
        if mode == 2:
            cmd = ['uname', '-m']
            stdout = subprocess.check_output(cmd)
            arch = stdout.replace('\n', '')
            print_padded_string("Architecture: " + arch)
    elif platform.system() == "Darwin":
        if mode == 0:
            cmd = ['uname', '-v']
            stdout = subprocess.check_output(cmd)
            stdout = stdout.replace('\n', '')
            stdout = stdout.split(':')[0]
            print_padded_string("Kernel: " + stdout)
        if mode == 1:
            cmd = ['uname', '-r']
            version = subprocess.check_output(cmd).replace('\n', '')
            cmd = ['uname', '-v']
            stdout = subprocess.check_output(cmd)
            stdout = stdout.replace('\n', '')
            stdout = stdout.replace(version + ':', version + '|')
            stdout = stdout.split('|')[-1]
            print_padded_string("Build:" + stdout)
        if mode == 2:
            cmd = ['uname', '-m']
            stdout = subprocess.check_output(cmd)
            arch = stdout.replace('\n', '')
            print_padded_string("Architecture: " + arch)
    else:
        if mode == 0:
            print_padded_string("Kernel: Unknown")
        if mode == 1:
            print_padded_string("Build: Unknown")
        if mode == 2:
            print_padded_string("Architecture: Unknown")


def print_line(func, parm=None):
    """ Print Line """

    print_vert_line()
    if parm is None:
        func()
    else:
        func(parm)
    print_vert_line(1)


def main():
    """ Module entrypoint """

    if sys.version_info < (2, 7, 0):
        print("Python Version must be at least 2.7!")
        sys.exit(1)

    _ = os.system("clear")

    print_horizontal_line()
    print_line(print_hostname)
    print_line(print_release)
    print_line(print_kernel_info, 0)
    print_line(print_kernel_info, 1)
    print_line(print_kernel_info, 2)

    print_horizontal_line()

if __name__ == '__main__':
    main()
