#!/usr/bin/perl -w
use File::Basename;

# 引数の処理
if (scalar @ARGV<2) {
  die "Usage: $0 task_list idx_for_output_file\n";
}
my $task_list = shift @ARGV;
my $output_idx = shift @ARGV;

# タスクリストの読み込み
open TASKS, "$task_list";
my @tasks = <TASKS>;
close TASKS;

# 各タスクに対して以下を繰り返す
# (1) 出力ファイルがあれば次のタスクへ
# (2) ロックファイルがあれば次のタスクへ
# (3) 出力ファイルもロックファイルもなければタスクを実行
foreach $task (@tasks) {
  chomp $task;
  # コマンドと引数
  my @comarg = split /[\s\t]+/, $task;
  # 出力ファイル
  my $output_file = $comarg[$output_idx];
  # ロックファイル
  my $lock_file = $output_file . '_lock';

  # (1) 出力ファイルの存在チェック
  if (-e "$output_file") {
    next;
  }

  # (2) ロック出力ファイルの存在チェック
  if (-e "$lock_file") {
    next;
  }

  # (3) タスクを実行
  mkdir "$lock_file";
  system "$task";
  rmdir "$lock_file";
}
