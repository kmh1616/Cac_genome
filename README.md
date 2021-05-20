# Cac_genome
Customized code/script for the paper "A chromosome-level Camptotheca acuminata genome assembly provides insights into the evolutionary origin of camptothecin biosynthesis".

regulate_coordi.py - use to covert gff file from contig version into chromosome version.

tandem_detect.py - use to find tandem repeat genes by using similarSequences.txt file from OrthoMCL and gene gff3 file.

count_every_species_gene_number.pl - use to count every species gene number in each gene famliy clustered by OrthoMCL group.txt file.

gene_number_and_length_count.pl - use to get gene numbers and length in the collinear blocks from MCScanX result .html file.

get_gene_from_group.pl - use to get genes of one species in the listed gene famlies from OrthoMCL group.txt file.

gene.pl - use to get genes in the gene families expanded and contracted using the out.cafe file.
