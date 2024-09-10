INPUT_vcf=A2M_chr12_9062708_9120919.fullassembled.BOTH.anno.phased.vcf.gz
INPUT_vcf=A4GNT_chr3_138118713_138137390.fullassembled.BOTH.anno.phased.vcf.gz

MERGE_vcf=${INPUT_vcf%.vcf.gz}.truvari_merge.vcf
COLLAPSE_vcf=${INPUT_vcf%.vcf.gz}.truvari_collapse.vcf
LOG=${INPUT_vcf%.vcf.gz}.truvari_collapse.log

DATA_DIR=../data/
OUT_DIR=$DATA_DIR/truvari/

truvari collapse -i $DATA_DIR/phased/$INPUT_vcf -o $OUT_DIR/$MERGE_vcf -c $OUT_DIR/$COLLAPSE_vcf >& $OUT_DIR/$LOG
