#！usr/bin/perl -w
use strict;
open LOG,"< groups.txt"||"cannot open a file";
open OUTPUT,"> number.txt"||"cannot open a file";

my @list;

while (my $line=<LOG>){
	chomp($line);
	@list=split /\s+/,$line;
my $Ara=0;
my $Cam=0;
my $Cat=0;
my $Cof=0;
my $Dau=0;
my $Lac=0;
my $Rho=0;
my $Vit=0;
	foreach my $list(@list){
	if($list=~/^Arabidopsis_thaliana/){$Ara++;}
	elsif($list=~/^Camptotheca_acuminata/){$Cam++;}
	elsif($list=~/^Catharanthus_roseus/){$Cat++;}
	elsif($list=~/^Coffea_canephora/){$Cof++;}
	elsif($list=~/^Daucus_carota/){$Dau++;}
	elsif($list=~/^Lactuca_sativa/){$Lac++;}
	elsif($list=~/^Rhododendron_delavayi/){$Rho++;}
	elsif($list=~/^Vitis_vinifera/){$Vit++;}
	print OUTPUT "$list[0]\tAra:$Ara\tCam:$Cam\tCat:$Cat\tCof:$Cof\tDau:$Dau\tLac:$Lac\tRho:$Rho\tVit:$Vit\n";
	}
}
close();
close();
