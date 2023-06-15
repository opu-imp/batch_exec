#!/usr/bin/perl -w

# 引数の処理
if (scalar @ARGV<2) {
  die "Usage: $0 input_fname output_fname\n";
}
my $input = shift @ARGV;
my $output = shift @ARGV;

# 引数の出力
print "$output\n";

# 2秒休憩
sleep 2;

# ファイルを出力
open OUT, "> $output";
print OUT "This is an output file.\n";
close OUT;
