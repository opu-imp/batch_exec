#!/usr/bin/perl -w

# �����ν���
if (scalar @ARGV<2) {
  die "Usage: $0 input_fname output_fname\n";
}
my $input = shift @ARGV;
my $output = shift @ARGV;

# �����ν���
print "$output\n";

# 2�õٷ�
sleep 2;

# �ե���������
open OUT, "> $output";
print OUT "This is an output file.\n";
close OUT;
