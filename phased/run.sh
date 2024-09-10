INPUT_vcf=A2M_chr12_9062708_9120919.fullassembled.BOTH.anno.vcf.gz
INPUT_vcf=A4GNT_chr3_138118713_138137390.fullassembled.BOTH.anno.vcf.gz

PHASED_vcf=${INPUT_vcf%.vcf.gz}.phased.vcf.gz

DATA_DIR=../data

./vcf_haplotype_merge.py -i $DATA_DIR/jogo/$INPUT_vcf -o $DATA_DIR/phased/$PHASED_vcf 
tabix -f $DATA_DIR/phased/$PHASED_vcf
