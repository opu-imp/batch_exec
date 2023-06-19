#!/usr/bin/perl -w
use File::Basename;

# �����ν���
if (scalar @ARGV<2) {
  die "Usage: $0 task_list idx_for_output_file\n";
}
my $task_list = shift @ARGV;
my $output_idx = shift @ARGV;

# �������ꥹ�Ȥ��ɤ߹���
open TASKS, "$task_list";
my @tasks = <TASKS>;
close TASKS;

# �ƥ��������Ф��ưʲ��򷫤��֤�
# (1) ���ϥե����뤬����м��Υ�������
# (2) ��å��ե����뤬����м��Υ�������
# (3) ���ϥե�������å��ե������ʤ���Х�������¹�
foreach $task (@tasks) {
  chomp $task;
  # ���ޥ�ɤȰ���
  my @comarg = split /[\s\t]+/, $task;
  # ���ϥե�����
  my $output_file = $comarg[$output_idx];
  # ��å��ե�����
  my $lock_file = $output_file . '_lock';

  # (1) ���ϥե������¸�ߥ����å�
  if (-e "$output_file") {
    next;
  }

  # (2) ��å����ϥե������¸�ߥ����å�
  if (-e "$lock_file") {
    next;
  }

  # (3) ��������¹�
  mkdir "$lock_file";
  system "$task";
  rmdir "$lock_file";
}
