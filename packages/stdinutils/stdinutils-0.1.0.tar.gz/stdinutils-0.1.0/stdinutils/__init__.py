import os

import sys

__version__ = '0.1.0'


def get_cmd(skip=1) -> str:
    return " ".join(sys.argv[skip:])


def get_arg(n=1) -> str:
    try:
        return sys.argv[n]
    except IndexError:
        return ""


def execute_pipe(cmd, line):
    os.system(f'echo "{line}" | {cmd}')


def execute(cmd, line):
    os.system(f'{cmd} {line}')


def execute_per_line_seg(cmd, line):
    for seg in line.split(" "):
        os.system(f'{cmd} {seg}')


def execute_per_line_seg_with_delim(cmd, line):
    for seg in line.split(get_arg()):
        cmd = get_cmd(2) or "echo"
        os.system(f'{cmd} {seg}')


def on_line(f, cmd, *args, **kwargs):
    line = sys.stdin.readline()
    while line != "":
        f(cmd, line, *args, **kwargs)
        line = sys.stdin.readline()
