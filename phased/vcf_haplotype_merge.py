#!/usr/bin/env python3

import pysam
import argparse

# コマンドライン引数を処理するための関数
def parse_args():
    parser = argparse.ArgumentParser(description="Merge haplotype columns in VCF to phased genotypes")
    parser.add_argument("-i", "--input", required=True, help="Input bgzip VCF file")
    parser.add_argument("-o", "--output", required=True, help="Output bgzip VCF file")
    return parser.parse_args()

# メイン処理
def main():
    args = parse_args()

    input_vcf = args.input  # コマンドライン引数で指定された入力ファイル
    output_vcf = args.output  # コマンドライン引数で指定された出力ファイル

    # VCFファイルをbgzip形式で開く
    with pysam.BGZFile(input_vcf, 'r') as infile, pysam.BGZFile(output_vcf, 'w') as outfile:
        for line in infile:
            line = line.decode()  # bgzipはバイナリ読み込みのため、デコードする
            if line.startswith("#"):  # ヘッダー行はそのままコピー
                if line.startswith("#CHROM"):
                    # サンプル名から ".hp1", ".hp2" を削除し、同じサンプルとして扱う
                    headers = line.strip().split("\t")
                    new_headers = headers[:9]  # フォーマットまでのフィールドを保持
                    sample_names = headers[9:]

                    # サンプル名を2つのハプロタイプを1つにまとめる
                    merged_samples = []
                    for i in range(0, len(sample_names), 2):
                        merged_samples.append(sample_names[i].replace(".hp1", ""))

                    new_headers += merged_samples
                    outfile.write(("\t".join(new_headers) + "\n").encode())
                else:
                    outfile.write((line + "\n").encode())  # ヘッダー行をそのまま出力
            else:
                fields = line.strip().split("\t")
                chrom, pos, var_id, ref, alt, qual, filt, info, fmt = fields[:9]
                genotype_data = fields[9:]

                # 新しいフィールドリストを作成
                new_genotype_data = []

                # 2つのハプロタイプをフェーズ済みのGTとしてマージ
                for i in range(0, len(genotype_data), 2):
                    gt_hp1 = genotype_data[i].split(":")[0]  # GTフィールドのみ取得
                    gt_hp2 = genotype_data[i + 1].split(":")[0]  # 2つ目のハプロタイプのGT

                    # ハプロタイプをフェーズ済みのGTに変換
                    if gt_hp1 == "." or gt_hp2 == ".":
                        new_gt = "."
                    else:
                        new_gt = f"{gt_hp1}|{gt_hp2}"

                    # 他のフォーマットフィールドをそのまま維持
                    other_fields_hp1 = ":".join(genotype_data[i].split(":")[1:])
                    # GTフィールドと他のフィールドを適切に結合
                    if other_fields_hp1:  # 空でなければ
                        new_genotype_data.append(f"{new_gt}:{other_fields_hp1}")
                    else:  # 空ならGTだけ
                        new_genotype_data.append(f"{new_gt}")

                # 新しいVCF行を作成
                new_fields = fields[:9] + new_genotype_data
                outfile.write(("\t".join(new_fields) + "\n").encode())

if __name__ == "__main__":
    main()
