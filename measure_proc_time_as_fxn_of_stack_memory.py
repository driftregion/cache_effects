#!/usr/bin/python3
import subprocess

M = 1024 * 1024 * 255

for k in [pow(2, n) for n in range(11)]:
    print(k)
    subprocess.check_call(['gcc', f'-DK={k}', f'-DARR_SIZE={M}', 'every_kth_item.c', '-o', 'every_kth_item'])
    subprocess.check_call(['time', './every_kth_item'])

"""
user time seems to drop from "significant" to "insignificant"
sys time stays about the same...
"""

"""
1
0.70user 0.32system 0:01.03elapsed 99%CPU (0avgtext+0avgdata 1045632maxresident)k
0inputs+0outputs (0major+261177minor)pagefaults 0swaps
2
0.40user 0.29system 0:00.70elapsed 99%CPU (0avgtext+0avgdata 1045760maxresident)k
0inputs+0outputs (0major+261179minor)pagefaults 0swaps
4
0.23user 0.31system 0:00.55elapsed 99%CPU (0avgtext+0avgdata 1045748maxresident)k
0inputs+0outputs (0major+261180minor)pagefaults 0swaps
8
0.17user 0.31system 0:00.49elapsed 99%CPU (0avgtext+0avgdata 1045748maxresident)k
0inputs+0outputs (0major+261182minor)pagefaults 0swaps
16
0.16user 0.32system 0:00.48elapsed 100%CPU (0avgtext+0avgdata 1045748maxresident)k
0inputs+0outputs (0major+261180minor)pagefaults 0swaps
32
0.14user 0.34system 0:00.49elapsed 99%CPU (0avgtext+0avgdata 1045696maxresident)k
0inputs+0outputs (0major+261178minor)pagefaults 0swaps
64
0.12user 0.30system 0:00.43elapsed 99%CPU (0avgtext+0avgdata 1045760maxresident)k
0inputs+0outputs (0major+261181minor)pagefaults 0swaps
128
0.09user 0.30system 0:00.40elapsed 98%CPU (0avgtext+0avgdata 1045748maxresident)k
0inputs+0outputs (0major+261180minor)pagefaults 0swaps
256
0.10user 0.29system 0:00.39elapsed 99%CPU (0avgtext+0avgdata 1045748maxresident)k
0inputs+0outputs (0major+261179minor)pagefaults 0swaps
512
0.06user 0.31system 0:00.38elapsed 100%CPU (0avgtext+0avgdata 1045640maxresident)k
0inputs+0outputs (0major+261178minor)pagefaults 0swaps
1024
0.07user 0.30system 0:00.38elapsed 98%CPU (0avgtext+0avgdata 1045744maxresident)k
0inputs+0outputs (0major+261181minor)pagefaults 0swaps
"""