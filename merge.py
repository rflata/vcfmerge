import argparse as ag
import variant as var

parser = ag.ArgumentParser(description='List of arguments')
parser.add_argument('-vcf1', '--vcfinputfile1', dest='vcf1', required=True)
parser.add_argument('-vcf2', '--vcfinputfile2', dest='vcf2', required=True)
parser.add_argument('-out', '--outputfile', dest='out', required=True)
args = parser.parse_args()

sample = args.vcf1.split('.')[0] + '|' + args.vcf2.split('.')[0]

with open(args.vcf1) as vcf1, open(args.vcf2) as vcf2:
    metaData = []
    vars1 = []
    for line in vcf1:
        if '##' in line:
            metaData.append(line.rstrip())
        elif '#CHROM' in line:
            header = line.rstrip()
        else:
            vars1.append(var.variant(line.rstrip().split('\t')))
    vars2 = []
    for line in vcf2:
        if '#' not in line:
            vars2.append(var.variant(line.rstrip().split('\t')))

    final = []
    for variant in vars1:
        if variant in vars2:
            variant.gt = '1|1'
            final.append(variant)
        else:
            variant.gt = '1|0'
            final.append(variant)
    for variant in vars2:
        if variant not in vars1:
            variant.gt = '0|1'
            final.append(variant)
    final.sort(key=lambda x:x.pos)

with open("merge.vcf","w") as merge:
    for i in metaData:
        merge.write(i + '\n')
    merge.write(header + '\t' + sample + '\n')
    for var in final:
        merge.write(var.chrom + '\t'+ var.pos +'\t' + var.id + '\t' + var.ref + '\t'+ var.alt + '\t' + var.qual + '\t' + var.filter + '\t' + var.info + '\t' + var.gt + '\n')

