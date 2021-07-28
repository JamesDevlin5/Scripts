#!/usr/bin/env python3

import argparse

fmt_color = lambda code: f'\033[{code}m'
fmt_header = lambda label: f'\t{fmt_color(34)}{label}: '
do_header = lambda label, pref, m: f'{fmt_header(label)}\t{fmt_color(37)}{pref}{fmt_color(36)}{m}{fmt_color(0)}'
num = 121

print(f"{fmt_color(35)}Information regarding:\t {fmt_color(4)}{fmt_color(33)}{num}{fmt_color(0)}\n")
print(do_header('Dec', '  ', num))
n = bin(num)
print(do_header('Bin', n[:2], n[2:]))
n = oct(num)
print(do_header('Oct', n[:2], n[2:]))
n = hex(num)
print(do_header('Hex', n[:2], n[2:]))

