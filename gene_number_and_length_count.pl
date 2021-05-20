my $file=shift;
my @filename=`ls ./nc_cp.html`;
my %h;
for(my $i=0;$i<@filename;$i++){
    open(A,"./nc_cp.html/$filename[$i]");
    <A>;
    my $name;
    if($filename[$i]=~m/(.+?)\.html/){
	$name=$1;
    }
    while(<A>){
	chomp;
	if(/<tr align='center'><td>(\d+)<\/td><td bgcolor='.+?'>(.+?)<\/td><td>/){
	    $h{$name}{$2}=$1;
	}
    }
    close(A);
}
my $number=0;
open(A,"$file");
my %h2;
while(<A>){
    chomp;
    my @a=split(/\t/);
    $h2{$a[1]}{1}=$a[2];
    $h2{$a[1]}{2}=$a[3];
}
close(A);
my $length=0;

foreach my $m(sort {$a cmp $b} keys %h){
    my $x;
    my $y;
    my $x1;
    my $y1;
    my $count=1;
    next if(keys %{$h{$m}}==1);
    foreach my $n(sort {$a cmp $b} keys %{$h{$m}}){
	if($h{$m}{$n}!=0){
	    if($count==1){
		$x1=$x;
		$x=$n;
		$count++;
	    }
	    $number++;
	    $y1=$y;
	    $y=$n;
	}
	else{
	    if(($y1 ne $y) && ($x1 ne $x) && $x && $y && ($y gt $x)){
		$length=$length+$h2{$y}{2}-$h2{$x}{$1}+1;
#		print "$x $y\n";
	    }
	    $count=1;
	    $x1=$x;
	    $x=$n;
	}
    }
    if(($y1 ne $y) && ($x1 ne $x) && $x && $y && ($y gt $x)){
	$length=$length+$h2{$y}{2}-$h2{$x}{$1}+1;
#	print "$x $y\n";
    }

}
print "$number $length\n";
