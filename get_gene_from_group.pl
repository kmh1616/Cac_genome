#file OCG $file1 group.txt 
my ($file,$file1) = @ARGV;
open(F,"$file");
open(F1,"$file1");
open(O,">$file.group");
open(O1,">$file.Cam");
my %hash;
while (<F>) {
	# body...
	chomp;
	$hash{$_}++;
}
while (<F1>) {
	# body...
	chomp;
	my @temp = split(/\s+/,$_);
	$temp[0] =~s/://g;
	if(exists $hash{$temp[0]}){
		print O "$_\n";
		for (my $i = 1; $i < @temp; $i++) {
			if($temp[$i]=~m/Cam.+?\|(.+)/){
				print O1 "$1\n";
			}
		}
	}
}

close(F);
close(F1);
close(O);
close(O1);