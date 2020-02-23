import sys
import subprocess

isd_file = sys.argv[1]

isd_f = open(isd_file, 'r')
for line in isd_f:
	seq = line[:-1].split('\t')[0]
	idd = line[:-1].split('\t')[1]
	tiss = line[:-1].split('\t')[2]



	subprocess.call(['python', 'Fasta.py', seq, idd, tiss])
	subprocess.call(['bowtie2', '-a', '-p', '6', '-x', 'GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.bowtie_index', '-U', idd+'.fa', '-f', '-S', idd+'.sam'])
	subprocess.call(['samtools', 'view', '-F', '4' '-bh', idd+'.sam', '-o', idd+'.bam'])
	subprocess.call(['samtools', 'sort', idd+'.bam', '-o', idd+'.sort.bam'])
	subprocess.call(['rm', idd+'.sam'])
	subprocess.call(['rm', idd+'.bam'])
	subprocess.call(['rm', idd+'.fa'])
	with open(idd+'.bg', 'w') as f, open(idd+'.err', 'w') as ferr:
		subprocess.call(['bedtools', 'genomecov', '-bg', '-ibam', idd+'.sort.bam'], stdout = f, stderr=ferr)

	subprocess.call(['python', 'interval.py', idd+'.bg', 'all.bed'])
isd_f.close()

