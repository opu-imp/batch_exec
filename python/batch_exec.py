#!/usr/bin/env python3
import os
import subprocess
import sys

# 引数の処理
if len(sys.argv) < 3:
    raise ValueError("Usage: {} task_list idx_for_output_file".format(sys.argv[0]))

task_list = sys.argv[1]
output_idx = int(sys.argv[2])

# タスクリストの読み込み
with open(task_list, 'r') as file:
    tasks = file.readlines()

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
    subprocess.run(task, shell=True)
    os.rmdir(lock_file)
