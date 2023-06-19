#!/usr/bin/env python3
import sys
import time

# 引数の処理
if len(sys.argv) < 3:
    raise ValueError("Usage: {} input_fname output_fname".format(sys.argv[0]))

input_fname = sys.argv[1]
output_fname = sys.argv[2]

# 引数の出力
print(output_fname)

# 2秒休憩
time.sleep(2)

# ファイルを出力
with open(output_fname, 'w') as file:
    file.write("This is an output file.\n")
