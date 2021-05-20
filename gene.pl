my $file = shift;
open(F,"$file");
my $number = 0;
open(O1,">$file.Expansion");
open(O2,">$file.Decrease");
#open(O3,">$file.Remain");
while (<F>) {
	# body...
	$number++;
	next if($number<=10);#第11行才开始OCG统计
	my @temp = split(/\s+/,$_);
	if($temp[1]=~m/nata_(\d+):.+?\)_(\d+):/){
		if($1>$2){
			print O1 "$temp[0]\n";
		}
		if($1<$2){
			print O2 "$temp[0]\n";
		}
		# if($1==$2){
		# 	print O3 "$temp[0]\n";
		# }
	}
}
close(F);
close(O1);
close(O2);
#close(O3);