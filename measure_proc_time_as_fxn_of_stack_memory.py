#!/usr/bin/python3
import subprocess

hmm = 'limit stacksize 2g'

for int_arr_size in [64 * 1024 * 1024]:
    subprocess.check_call(['gcc', f'-DARR_SIZE={int_arr_size}', 'loop.c', '-o', 'loop'])
    for case in [1, 2]:
        print(subprocess.check_call(['time', './loop', str(case)]))

for k in [pow(n, 2) for n in range(10)]:
    subprocess.check_call(['gcc', f'-DK={k}', 'every_kth_item.c', '-o', 'every_kth_item'])
    subprocess.check_call(['time', './every_kth_item'])
