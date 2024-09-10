#!/bin/bash

INPUT_vcf=A2M_chr12_9062708_9120919.fullassembled.BOTH.anno.phased.vcf.gz
INPUT_vcf=A4GNT_chr3_138118713_138137390.fullassembled.BOTH.anno.phased.vcf.gz
REFERENCE_FASTA=hg38.fa.gz

DATA_DIR=/data/mitsuhashi/jogo/data
OUTDIR_RUN1=$DATA_DIR/part/results/part1
OUTDIR_RUN2=$DATA_DIR/part/results/part2
TMPDIR=/tmp

PANPOP_DIR=/data/mitsuhashi/panpop

rm -rf $OUTDIR_RUN1
rm -rf $OUTDIR_RUN2

#perl ../bin/PART_run.pl --in_vcf $INPUT_vcf -o $OUTDIR_RUN1 -r $REFERENCE_FASTA  -t 16 --tmpdir $TMPDIR

perl $PANPOP_DIR/bin/PART_run.pl --in_vcf $DATA_DIR/phased/$INPUT_vcf -o $OUTDIR_RUN1 -r $DATA_DIR/$REFERENCE_FASTA  -t 16

#perl ../bin/PART_run.pl --in_vcf $OUTDIR_RUN1/3.final.vcf.gz -o $OUTDIR_RUN2 -r $REFERENCE_FASTA -t 16 --tmpdir $TMPDIR -not_first_merge
