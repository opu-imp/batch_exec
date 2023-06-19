#!/usr/bin/env python3
import os
import subprocess
import sys
import torch

# 引数の処理
if len(sys.argv) < 4:
    raise ValueError("Usage: {} task_list idx_for_output_file gpu_lock_path".format(sys.argv[0]))

task_list = sys.argv[1]
output_idx = int(sys.argv[2])
gpu_lock_path = sys.argv[3]

# タスクリストの読み込み
with open(task_list, 'r') as file:
    tasks = file.readlines()

# 使用できるGPU IDの列挙
num_gpus = torch.cuda.device_count()

# 使用するGPUの決定
gpu_lock_file = ""
gpuid = ""
gpu_arg = ""
for id in range(num_gpus):
    gpu_lock_file = "{}/gpuid_lock-{}".format(gpu_lock_path, id)
    # ロックファイル(ディレクトリ)が存在しなかったら、作成して、処理を終える
    if not os.path.exists(gpu_lock_file):
        gpuid = id
        gpu_arg = "--gpu_id {}".format(id)
        print("GPU {} will be used".format(gpuid))
        os.mkdir(gpu_lock_file)
        break

if gpu_arg=="":
    print("No GPU is available")
    sys.exit()

# 各タスクに対して以下を繰り返す
# (1) 出力ファイルがあれば次のタスクへ
# (2) ロックファイルがあれば次のタスクへ
# (3) 出力ファイルもロックファイルもなければタスクを実行
for task in tasks:
    task = task.strip()
    # コマンドと引数
    comarg = task.split()
    # 出力ファイル
    output_file = comarg[output_idx]
    # ロックファイル
    lock_file = output_file + '_lock'

    # (1) 出力ファイルの存在チェック
    if os.path.exists(output_file):
        continue

    # (2) ロック出力ファイルの存在チェック
    if os.path.exists(lock_file):
        continue

    # (3) タスクを実行
    os.mkdir(lock_file)
    subprocess.run(task+" "+gpu_arg, shell=True)
    os.rmdir(lock_file)

# GPUロックフィアル(ディレクトリ)を削除する
os.rmdir(gpu_lock_file)
print("GPU {} is released".format(gpuid))
